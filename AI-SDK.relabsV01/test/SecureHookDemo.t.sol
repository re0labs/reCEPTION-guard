// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import "../contracts/SecureHookDemo.sol";

contract SecureHookDemoTest is Test {
    SecureHookDemo hook;

    address poolManager = address(100);
    address user = address(200);
    address attacker = address(300);

    function setUp() public {
        hook = new SecureHookDemo(poolManager);

        vm.deal(user, 10 ether);
        vm.deal(attacker, 10 ether);
    }

    function testDepositWorks() public {
        vm.prank(user);
        hook.deposit{value: 1 ether}();

        assertEq(hook.balances(user), 1 ether);
    }

    function testWithdrawWorks() public {
        vm.startPrank(user);
        hook.deposit{value: 1 ether}();
        hook.withdraw(0.4 ether);
        vm.stopPrank();

        assertEq(hook.balances(user), 0.6 ether);
    }

    function testBeforeSwapOnlyPoolManager() public {
        vm.prank(poolManager);
        bytes4 result = hook.beforeSwap(address(1), bytes("abc"));
        assertEq(result, hook.beforeSwap.selector);
    }

    function testBeforeSwapRevertsForNonPoolManager() public {
        vm.prank(user);
        vm.expectRevert();
        hook.beforeSwap(address(1), bytes("abc"));
    }

    function testAfterSwapOnlyPoolManager() public {
        vm.prank(poolManager);
        bytes4 result = hook.afterSwap(10, -10);
        assertEq(result, hook.afterSwap.selector);
    }

    function testAfterSwapRevertsOnZeroDeltas() public {
        vm.prank(poolManager);
        vm.expectRevert();
        hook.afterSwap(0, 0);
    }

    function testDeltaAdjustmentValidationPasses() public {
        bool ok = hook.simulateDeltaAdjustment(10, 12);
        assertTrue(ok);
    }

    function testDeltaAdjustmentValidationRevertsOnSignFlip() public {
        vm.expectRevert();
        hook.simulateDeltaAdjustment(10, -5);
    }
}

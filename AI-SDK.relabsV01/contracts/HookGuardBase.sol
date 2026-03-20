// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

abstract contract HookGuardBase {
    address public immutable poolManager;

    error NotPoolManager();
    error ZeroAddress();

    constructor(address _poolManager) {
        if (_poolManager == address(0)) revert ZeroAddress();
        poolManager = _poolManager;
    }

    modifier onlyPoolManager() {
        if (msg.sender != poolManager) revert NotPoolManager();
        _;
    }

    function _checkNotZero(address target) internal pure {
        if (target == address(0)) revert ZeroAddress();
    }
}

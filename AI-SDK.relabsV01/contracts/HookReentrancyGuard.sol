// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

abstract contract HookReentrancyGuard {
    uint256 private constant _NOT_ENTERED = 1;
    uint256 private constant _ENTERED = 2;

    uint256 private _status = _NOT_ENTERED;

    error ReentrancyBlocked();

    modifier nonReentrant() {
        if (_status == _ENTERED) revert ReentrancyBlocked();

        _status = _ENTERED;
        _;
        _status = _NOT_ENTERED;
    }
}

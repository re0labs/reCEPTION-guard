// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

library DeltaValidation {
    error InvalidDelta();
    error SuspiciousDeltaAdjustment();

    function validateSwapDelta(
        int256 amount0Delta,
        int256 amount1Delta
    ) internal pure {
        // Demo rule:
        // At least one delta should be non-zero in a meaningful swap path.
        if (amount0Delta == 0 && amount1Delta == 0) {
            revert InvalidDelta();
        }
    }

    function validateLiquidityDelta(
        int256 liquidityDelta
    ) internal pure {
        // Demo rule:
        // Liquidity delta should not be zero for actual liquidity changes.
        if (liquidityDelta == 0) {
            revert InvalidDelta();
        }
    }

    function validateAdjustedDelta(
        int256 originalDelta,
        int256 adjustedDelta
    ) internal pure {
        // Demo heuristic:
        // suspicious if adjustment flips sign unexpectedly
        if (
            (originalDelta > 0 && adjustedDelta < 0) ||
            (originalDelta < 0 && adjustedDelta > 0)
        ) {
            revert SuspiciousDeltaAdjustment();
        }
    }
}

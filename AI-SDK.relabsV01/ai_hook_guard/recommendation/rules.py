RULES = {
    "reentrancy": {
        "recommendation": (
            "Protect the hook against reentrant execution and update internal state "
            "before making external calls."
        ),
        "patch": (
            "Move state updates before external interactions and consider a "
            "reentrancy guard."
        )
    },

    "state_corruption_risk": {
        "recommendation": (
            "Review state transitions carefully and avoid overwriting, resetting, "
            "or inconsistently mutating critical state variables."
        ),
        "patch": (
            "Refactor state updates so they happen in a safe order, and add checks "
            "to preserve invariant consistency."
        )
    },

    "unsafe_external_call": {
        "recommendation": (
            "Avoid unsafe low-level external calls unless strictly necessary. "
            "Validate targets and always verify call success."
        ),
        "patch": (
            "Wrap low-level calls with success checks, restrict callable targets, "
            "and avoid external execution before critical state updates."
        )
    },

    "missing_poolmanager_verification": {
        "recommendation": (
            "Ensure that hook entrypoints can only be called by the expected "
            "PoolManager."
        ),
        "patch": (
            "Add a sender check such as require(msg.sender == poolManager) or use "
            "an onlyPoolManager modifier."
        )
    },

    "incorrect_delta_accounting": {
        "recommendation": (
            "Review swap and liquidity delta calculations to ensure accounting "
            "matches expected hook and pool invariants."
        ),
        "patch": (
            "Validate delta updates carefully, avoid arbitrary delta adjustments, "
            "and add tests covering amount0Delta, amount1Delta, and balanceDelta flows."
        )
    }
}

def detect_incorrect_delta_accounting(code):

    delta_keywords = [
        "delta",
        "balanceDelta",
        "beforeDelta",
        "afterDelta",
        "amount0Delta",
        "amount1Delta"
    ]

    found_delta_logic = False

    for keyword in delta_keywords:
        if keyword in code:
            found_delta_logic = True
            break

    suspicious_patterns = [
        "delta +",
        "delta -",
        "= delta",
        "balanceDelta +",
        "balanceDelta -",
        "amount0Delta +",
        "amount1Delta +"
    ]

    suspicious_found = False

    for pattern in suspicious_patterns:
        if pattern in code:
            suspicious_found = True
            break

    if found_delta_logic and suspicious_found:
        return {
            "found": True,
            "details": "Potential incorrect delta accounting detected"
        }

    return {
        "found": False,
        "details": None
    }

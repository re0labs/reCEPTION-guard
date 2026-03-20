def detect_state_corruption_risk(code):

    risky_patterns = [
        "balance = 0",
        "totalSupply = 0",
        "reserve = 0",
        "liquidity = 0",
        "+=",
        "-="
    ]

    matches = 0

    for pattern in risky_patterns:
        if pattern in code:
            matches += 1

    if matches >= 2:
        return {
            "found": True,
            "details": "Multiple state changes detected that may lead to inconsistent or corrupted state"
        }

    return {
        "found": False,
        "details": None
    }

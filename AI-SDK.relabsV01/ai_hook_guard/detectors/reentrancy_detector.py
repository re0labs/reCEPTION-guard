def detect_reentrancy(code):
    if "call{" in code or "call.value" in code or ".call(" in code:
        return {
            "found": True,
            "details": "External call detected before state update (possible reentrancy)"
        }

    return {
        "found": False,
        "details": None
    }

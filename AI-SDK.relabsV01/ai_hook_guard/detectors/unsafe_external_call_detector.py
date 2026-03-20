def detect_unsafe_external_call(code):

    if ".call(" in code or "call{" in code or ".delegatecall(" in code or ".staticcall(" in code:
        return {
            "found": True,
            "details": "Unsafe low-level external call detected"
        }

    return {
        "found": False,
        "details": None
    }

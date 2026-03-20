def detect_missing_poolmanager_verification(code):

    hook_keywords = [
        "beforeSwap",
        "afterSwap",
        "beforeAddLiquidity",
        "afterAddLiquidity",
        "beforeRemoveLiquidity",
        "afterRemoveLiquidity",
        "beforeInitialize",
        "afterInitialize"
    ]

    hook_found = False

    for keyword in hook_keywords:
        if keyword in code:
            hook_found = True
            break

    has_poolmanager_check = (
        "msg.sender == poolManager" in code or
        "require(msg.sender == poolManager" in code or
        "onlyPoolManager" in code
    )

    if hook_found and not has_poolmanager_check:
        return {
            "found": True,
            "details": "Hook function detected without PoolManager verification"
        }

    return {
        "found": False,
        "details": None
    }

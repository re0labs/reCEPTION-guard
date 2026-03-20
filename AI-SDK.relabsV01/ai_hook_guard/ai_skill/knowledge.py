# ai_skill/knowledge.py

HOOK_SECURITY_KNOWLEDGE = {
    "beforeSwap": {
        "risk": "delta manipulation",
        "check": "validate returned delta",
        "fix": "ensure pool state consistency"
    },
    "afterSwap": {
        "risk": "fee override attack",
        "check": "verify fee bounds",
        "fix": "limit fee changes"
    },
    "reentrancy": {
        "pattern": "call(",
        "fix": "use checks-effects-interactions"
    }
}

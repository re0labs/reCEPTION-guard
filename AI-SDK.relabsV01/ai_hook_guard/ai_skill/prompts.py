# ai_skill/prompts.py

def build_prompt(code, findings):

    return f"""
You are a smart contract security expert specialized in Uniswap v4 hooks.

Analyze the code and findings:

CODE:
{code}

DETECTED ISSUES:
{findings}

Tasks:
1. Explain vulnerabilities
2. Suggest secure fixes
3. Return improved code
"""

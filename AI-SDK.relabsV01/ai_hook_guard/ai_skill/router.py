import os
from .offline_engine import run_offline_ai_skill

try:
    from .engine import run_ai_skill as run_online_ai_skill
except Exception:
    run_online_ai_skill = None


def run_ai_analysis(code: str, findings: list):
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key and run_online_ai_skill is not None:
        try:
            return run_online_ai_skill(code, findings)
        except Exception:
            return run_offline_ai_skill(code, findings)

    return run_offline_ai_skill(code, findings)

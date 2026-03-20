from .analyzer import Analyzer
from .scoring.risk_engine import RiskEngine
from .config import Config


class HookGuard:

    def __init__(self):
        self.config = Config()
        self.analyzer = Analyzer()
        self.risk_engine = RiskEngine()

    def configure(self, settings):
        for k, v in settings.items():
            setattr(self.config, k, v)

    def validate(self, code):

        analysis = self.analyzer.analyze(code)
        risk = self.risk_engine.compute(analysis)
        approved = risk < self.config.risk_threshold

        return {
            "approved": approved,
            "risk_score": risk,
            "issues": analysis.get("issues", []),
            "findings": analysis.get("findings", []),
            "fixed_code": analysis.get("patched_code", code),
            "ai_analysis": analysis.get("ai_analysis", {}),
            "confidence": 0.8
        }


hook_guard = HookGuard()

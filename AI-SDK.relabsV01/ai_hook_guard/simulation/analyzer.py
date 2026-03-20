from .detectors.reentrancy_detector import detect_reentrancy
from .detectors.state_corruption_risk_detector import detect_state_corruption_risk
from .detectors.unsafe_external_call_detector import detect_unsafe_external_call
from .detectors.missing_poolmanager_verification_detector import detect_missing_poolmanager_verification
from .detectors.incorrect_delta_accounting_detector import detect_incorrect_delta_accounting

from .recommendation.recommender import Recommender
from .ai_skill.engine import run_ai_skill


class Analyzer:

    def __init__(self):
        self.recommender = Recommender()

    def analyze(self, code):

        issues = []
        findings = []

        # --- Detector layer ---
        reentrancy = detect_reentrancy(code)
        state_corruption_risk = detect_state_corruption_risk(code)
        unsafe_external_call = detect_unsafe_external_call(code)
        missing_poolmanager_verification = detect_missing_poolmanager_verification(code)
        incorrect_delta_accounting = detect_incorrect_delta_accounting(code)

        if reentrancy["found"]:
            findings.append({
                "type": "reentrancy",
                "description": "Potential reentrancy vulnerability detected",
                "severity": "high",
                "details": reentrancy["details"]
            })
            issues.append("reentrancy")

        if state_corruption_risk["found"]:
            findings.append({
                "type": "state_corruption_risk",
                "description": "Potential state corruption risk detected",
                "severity": "medium",
                "details": state_corruption_risk["details"]
            })
            issues.append("state_corruption_risk")

        if unsafe_external_call["found"]:
            findings.append({
                "type": "unsafe_external_call",
                "description": "Potential unsafe external call detected",
                "severity": "high",
                "details": unsafe_external_call["details"]
            })
            issues.append("unsafe_external_call")

        if missing_poolmanager_verification["found"]:
            findings.append({
                "type": "missing_poolmanager_verification",
                "description": "Missing PoolManager verification detected",
                "severity": "high",
                "details": missing_poolmanager_verification["details"]
            })
            issues.append("missing_poolmanager_verification")

        if incorrect_delta_accounting["found"]:
            findings.append({
                "type": "incorrect_delta_accounting",
                "description": "Potential incorrect delta accounting detected",
                "severity": "medium",
                "details": incorrect_delta_accounting["details"]
            })
            issues.append("incorrect_delta_accounting")

        # --- Recommendation layer ---
        recommendation_results = self.recommender.recommend(issues)

        recommendation_map = {
            item["issue"]: item for item in recommendation_results
        }

        for finding in findings:
            rec = recommendation_map.get(finding["type"], {})
            finding["recommendation"] = rec.get("recommendation", "")
            finding["patch"] = rec.get("patch", "")

        # --- AI skill layer ---
        ai_analysis = run_ai_skill(code, findings)

        return {
            "issues": issues,
            "findings": findings,
            "ai_analysis": ai_analysis,
            "patched_code": code
        }

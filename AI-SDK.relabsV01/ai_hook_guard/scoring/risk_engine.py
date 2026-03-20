class RiskEngine:

    def compute(self, analysis):

        risk = 0.0

        for issue in analysis.get("issues", []):
            if issue == "reentrancy":
                risk += 0.7
            elif issue == "missing_poolmanager_verification":
                risk += 0.6
            elif issue == "incorrect_delta_accounting":
                risk += 0.6
            elif issue == "unsafe_external_call":
                risk += 0.4
            elif issue == "state_corruption_risk":
                risk += 0.5
            else:
                risk += 0.2

        return min(risk, 1.0)

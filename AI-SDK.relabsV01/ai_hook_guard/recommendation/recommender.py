from .rules import RULES


class Recommender:

    def recommend(self, issues):
        results = []

        for issue in issues:
            if issue in RULES:
                results.append({
                    "issue": issue,
                    "recommendation": RULES[issue]["recommendation"],
                    "patch": RULES[issue]["patch"]
                })
            else:
                results.append({
                    "issue": issue,
                    "recommendation": "No recommendation available yet.",
                    "patch": "No patch available yet."
                })

        return results

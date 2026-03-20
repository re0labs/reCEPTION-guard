def compute_reward(result, action):

    risk = result.get("risk_score", 0)

    # 🎯 Strategy
    if action == 1 and risk > 0:
        return +10  # fixed vulnerability

    if action == 0 and risk > 0:
        return -10  # ignored risk

    if risk == 0:
        return +5  # safe

    return 0

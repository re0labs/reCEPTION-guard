import random
from ai_hook_guard.simulation.environment import AttackEnvironment

def main():

    env = AttackEnvironment()

    for i in range(10):

        print(f"\n=== ITERATION {i} ===")

        # 🔄 Reset environment
        state = env.reset()
        print("Initial Contract:\n", state)

        # 🎯 Random action (simulate agent)
        action = random.choice([0, 1])
        print("Action:", action)

        # ▶️ Step
        result = env.step(action)

        print("\n--- RESULT ---")
        print("Reward:", result["reward"])
        print("Risk Score:", result["analysis"].get("risk_score"))
        print("Issues:", result["analysis"].get("issues"))
        print("Done:", result["done"])

if __name__ == "__main__":
    main()

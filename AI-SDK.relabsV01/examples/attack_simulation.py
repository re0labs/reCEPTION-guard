import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
from ai_hook_guard.simulation.environment import AttackEnvironment

env = AttackEnvironment()

for i in range(10):

    state = env.reset()

    action = random.choice([0, 1])  # simulate agent

    result = env.step(action)

    print("Iteration:", i)
    print("Action:", action)
    print("Reward:", result["reward"])
    print("Risk:", result["analysis"]["risk_score"])
    print("Done:", result["done"])
    print()

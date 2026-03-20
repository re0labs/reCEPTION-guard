from ai_hook_guard.guard import hook_guard
from .attacker_agent import AttackerAgent
from .reward import compute_reward


class AttackEnvironment:

    def __init__(self):

        self.agent = AttackerAgent()
        self.state = None
        self.done = False

    # --------------------------
    # 🔄 RESET
    # --------------------------
    def reset(self):
        """Start new episode"""
        self.state = self.agent.generate_attack()
        self.done = False
        return self.state

    # --------------------------
    # ▶️ STEP (CORE RL)
    # --------------------------
    def step(self, action=None):
        """
        action:
            0 = do nothing
            1 = apply fix
        """

        if self.state is None:
            self.reset()

        contract = self.state

        # 🔧 APPLY ACTION
        modified_contract = self._apply_action(contract, action)

        # 🔍 Analyze
        result = hook_guard.validate(modified_contract)

        # 🎯 Reward
        reward = compute_reward(result, action)

        # 🧠 Next state (optional for now)
        next_state = modified_contract

        # 🏁 End episode (simple version)
        self.done = True

        return {
            "state": contract,
            "action": action,
            "next_state": next_state,
            "analysis": result,
            "reward": reward,
            "done": self.done
        }

    # --------------------------
    # 🔧 ACTION LOGIC
    # --------------------------
    def _apply_action(self, contract, action):

        if action == 1:
            # Example fix (very simple)
            if "call{" in contract:
                return contract.replace(
                    "msg.sender.call{value:amount}(\"\");",
                    "require(!locked);\nlocked = true;\nmsg.sender.call{value:amount}(\"\");\nlocked = false;"
                )

        return contract

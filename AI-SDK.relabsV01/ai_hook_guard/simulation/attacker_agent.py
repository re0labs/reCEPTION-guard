import random
from .contract_generator import generate_contract

class AttackerAgent:

    def __init__(self):
        self.strategy = "random"

    def generate_attack(self):

        contract = generate_contract()

        return contract

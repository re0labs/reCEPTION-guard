import random

TEMPLATES = [

"""
function withdraw(uint amount) public {
    msg.sender.call{value:amount}("");
}
""",

"""
function withdraw(uint amount) public {
    (bool success,) = msg.sender.call{value:amount}("");
    require(success);
}
""",

"""
function withdraw(uint amount) public nonReentrant {
    payable(msg.sender).transfer(amount);
}
"""

]

def generate_contract():

    return random.choice(TEMPLATES)

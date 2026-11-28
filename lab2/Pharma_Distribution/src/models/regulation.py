class Regulation:
    def __init__(self, name: str): self.name, self.rules = name, []
    def add_rule(self, r: str): self.rules.append(r)
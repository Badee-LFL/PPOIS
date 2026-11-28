class Discount:
    def __init__(self, pct: float, valid_until: str): self.pct, self.valid_until = pct, valid_until
    def apply(self, total: float) -> float: return total * (1 - self.pct / 100)
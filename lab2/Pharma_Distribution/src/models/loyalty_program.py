class LoyaltyProgram:
    def __init__(self, client): self.client, self.points = client, 0
    def add_points(self, amt: float): self.points += int(amt)
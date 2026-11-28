class Insurance:
    def __init__(self, provider: str, cov: float): self.provider, self.cov = provider, cov
    def file_claim(self, amt: float) -> float: return min(amt, self.cov)
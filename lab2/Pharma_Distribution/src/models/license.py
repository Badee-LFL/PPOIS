class License:
    def __init__(self, num: str, exp: str): self.num, self.exp = num, exp
    def check_valid(self, curr: str) -> bool: return curr <= self.exp
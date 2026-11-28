class SerialNumber:
    def __init__(self, num: str): self.num, self.is_invalidated = num, False
    def invalidate(self): self.is_invalidated = True
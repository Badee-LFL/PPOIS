class Recall:
    def __init__(self, batch, reason: str): self.batch, self.reason, self.is_active = batch, reason, True
    def execute(self): self.batch.mark_expired(); self.is_active = False
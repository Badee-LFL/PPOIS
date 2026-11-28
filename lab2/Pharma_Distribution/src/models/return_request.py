class ReturnRequest:
    def __init__(self, order, reason: str): self.order, self.reason, self.status = order, reason, "Pending"
    def approve(self): self.status = "Approved"
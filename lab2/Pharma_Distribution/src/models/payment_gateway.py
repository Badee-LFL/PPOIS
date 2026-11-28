class PaymentGateway:
    def __init__(self, name: str): self.name = name
    def authorize(self, amt: float) -> bool: return amt > 0
from src.exceptions import PaymentFailedException
class Payment:
    def __init__(self, amount: float, method: str):
        self.amount = amount
        self.method = method
        self.status = "Pending"
    def process(self, invoice):
        if self.amount < invoice.total:
            raise PaymentFailedException("Insufficient funds.")
        self.status = "Completed"
        invoice.mark_paid()
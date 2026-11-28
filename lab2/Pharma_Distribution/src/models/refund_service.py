class RefundService:
    def __init__(self): self.refunds = []
    def process_refund(self, payment, amt: float):
        self.refunds.append({"payment": payment, "amount": amt}); payment.status = "Refunded"
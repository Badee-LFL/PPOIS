class Invoice:
    def __init__(self, invoice_id: str, order):
        self.invoice_id = invoice_id
        self.order = order
        self.total = order.calculate_total()
        self.is_paid = False
    def mark_paid(self):
        self.is_paid = True
class ReorderPlanner:
    def __init__(self, analyzer): self.analyzer, self.pending_orders = analyzer, []
    def create_reorder(self, qty: int): self.pending_orders.append(qty)
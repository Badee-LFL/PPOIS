from src.exceptions import SupplierNotApprovedException
class Supplier:
    def __init__(self, name: str, email: str):
        self.name, self.email, self.is_approved, self.batches = name, email, False, []
    def approve(self): self.is_approved = True
    def supply_batch(self, batch):
        if not self.is_approved: raise SupplierNotApprovedException("Not approved")
        self.batches.append(batch)
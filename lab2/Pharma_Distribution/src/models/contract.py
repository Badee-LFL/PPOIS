class Contract:
    def __init__(self, contract_id: str, supplier, months: int):
        self.contract_id, self.supplier, self.months, self.is_active = contract_id, supplier, months, True
    def terminate(self): self.is_active = False
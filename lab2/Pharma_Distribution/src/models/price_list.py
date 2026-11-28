class PriceList:
    def __init__(self, name: str): self.name, self.entries = name, {}
    def add_entry(self, med, price: float): self.entries[med.name] = price
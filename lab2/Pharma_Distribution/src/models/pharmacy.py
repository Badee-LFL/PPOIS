from .client import Client

class Pharmacy(Client):
    def __init__(self, name: str, license: str):
        super().__init__(name, "Pharmacy")
        self.license = license
        self.inventory = []
        
    def request_restock(self, medicine, qty: int):
        self.inventory.append({"medicine": medicine, "qty": qty})
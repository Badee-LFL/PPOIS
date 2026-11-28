from src.exceptions import InvalidMedicineDataException
class Medicine:
    def __init__(self, name: str, dosage: str, requires_prescription: bool):
        if not name or not dosage:
            raise InvalidMedicineDataException("Missing data")
        self.name = name
        self.dosage = dosage
        self.requires_prescription = requires_prescription
        self.price = 0.0
        self.batches = []
    def set_price(self, price: float):
        if price < 0:
            raise InvalidMedicineDataException("Negative price")
        self.price = price
    def attach_batch(self, batch):
        self.batches.append(batch)
    def calculate_available_stock(self) -> int:
        return sum(b.quantity for b in self.batches if not b.is_expired)
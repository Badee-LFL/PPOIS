from src.exceptions import InsufficientStockException
class Batch:
    def __init__(self, batch_number: str, medicine, quantity: int, expiry_date: str):
        self.batch_number = batch_number
        self.medicine = medicine
        self.quantity = quantity
        self.expiry_date = expiry_date
        self.is_expired = False
    def mark_expired(self):
        self.is_expired = True
    def deduct_quantity(self, amount: int):
        if amount > self.quantity:
            raise InsufficientStockException("Not enough")
        self.quantity -= amount
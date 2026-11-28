class OrderLine:
    def __init__(self, medicine, quantity: int):
        self.medicine = medicine
        self.quantity = quantity
    def calculate_subtotal(self) -> float:
        return self.medicine.price * self.quantity
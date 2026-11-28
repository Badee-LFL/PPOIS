class OrderLine:
    def __init__(self, medicine, quantity: int): self.medicine, self.quantity = medicine, quantity
    def calculate_subtotal(self) -> float: return self.medicine.price * self.quantity
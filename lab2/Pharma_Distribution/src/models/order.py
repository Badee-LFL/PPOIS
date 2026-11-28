from src.exceptions import InvalidOrderStateException, InsufficientStockException
class Order:
    def __init__(self, order_id: int, client):
        self.order_id = order_id
        self.client = client
        self.lines = []
        self.state = "Draft"
    def add_line(self, line):
        if self.state != "Draft":
            raise InvalidOrderStateException("Order already submitted.")
        self.lines.append(line)
    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.lines)
    def submit(self):
        for line in self.lines:
            if line.medicine.calculate_available_stock() < line.quantity:
                raise InsufficientStockException("Not enough stock.")
        self.state = "Submitted"
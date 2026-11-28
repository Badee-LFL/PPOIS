class Client:
    def __init__(self, name: str):
        self.name, self.orders = name, []
    def place_order(self, order): self.orders.append(order)
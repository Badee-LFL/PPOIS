class Client:
    def __init__(self, name: str, client_type: str):
        self.name = name
        self.client_type = client_type
        self.orders = []
    def place_order(self, order):
        self.orders.append(order)
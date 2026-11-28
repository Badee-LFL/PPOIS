class Warehouse:
    def __init__(self, name: str):
        self.name = name
        self.current_stock = 0
    def get_name(self):
        return self.name
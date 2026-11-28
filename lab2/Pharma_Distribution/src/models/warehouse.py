from src.exceptions import WarehouseCapacityException
class Warehouse:
    def __init__(self, location: str, capacity: int):
        self.location, self.capacity, self.current_stock = location, capacity, 0
    def add_stock(self, amount: int):
        if self.current_stock + amount > self.capacity: raise WarehouseCapacityException("Full")
        self.current_stock += amount
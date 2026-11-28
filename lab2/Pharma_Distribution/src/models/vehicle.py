class Vehicle:
    def __init__(self, plate: str, capacity: float, is_refrigerated: bool):
        self.plate, self.capacity, self.is_refrigerated = plate, capacity, is_refrigerated
    def check_capacity(self, w: float):
        if w > self.capacity: raise ValueError("Overloaded")
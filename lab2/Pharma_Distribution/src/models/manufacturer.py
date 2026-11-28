class Manufacturer:
    def __init__(self, name: str):
        self.name = name
        self.medicines = []

    def add_medicine(self, medicine):
        self.medicines.append(medicine)
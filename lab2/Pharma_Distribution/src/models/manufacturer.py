class Manufacturer:
    def __init__(self, name: str, country: str):
        self.name = name
        self.country = country
        self.medicines = []
    def add_medicine(self, medicine):
        self.medicines.append(medicine)
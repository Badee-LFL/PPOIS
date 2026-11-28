from .client import Client

class Hospital(Client):
    def __init__(self, name: str, beds: int):
        super().__init__(name, "Hospital")
        self.beds = beds
        
    def request_emergency_supply(self, medicine):
        return f"Emergency: {medicine.name}"
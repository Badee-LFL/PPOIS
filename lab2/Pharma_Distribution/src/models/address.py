class Address:
    def __init__(self, street: str, city: str, zip_code: str): self.street, self.city, self.zip_code = street, city, zip_code
    def format_address(self) -> str: return f"{self.street}, {self.city}, {self.zip_code}"
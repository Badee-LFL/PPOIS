class Barcode:
    def __init__(self, code: str): self.code = code
    def scan(self) -> str: return f"Scanned {self.code}"
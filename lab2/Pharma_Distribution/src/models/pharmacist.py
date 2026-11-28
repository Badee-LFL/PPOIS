from src.exceptions import PrescriptionRequiredException

class Pharmacist:
    def __init__(self, name: str, license: str):
        self.name = name
        self.license = license

    def dispense(self, prescription):
        if not prescription.is_valid:
            raise PrescriptionRequiredException("Invalid prescription.")
        prescription.is_dispensed = True
class Doctor:
    def __init__(self, name: str, license_number: str):
        self.name = name
        self.license_number = license_number

    def write_prescription(self, medicine, patient_name: str):
        from .prescription import Prescription
        return Prescription(patient_name, self, medicine)
class Prescription:
    def __init__(self, patient_name: str, doctor, medicine):
        self.patient_name = patient_name
        self.doctor = doctor
        self.medicine = medicine
        self.is_valid = True
        self.is_dispensed = False

    def invalidate(self):
        self.is_valid = False
class DemandForecaster:
    def __init__(self, medicine): self.medicine = medicine
    def forecast_next_month(self) -> int: return len(self.medicine.batches) * 100
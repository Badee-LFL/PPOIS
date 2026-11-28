class TemperatureLog:
    def __init__(self, zone): self.zone, self.logs = zone, []
    def log_temperature(self, temp: float):
        self.zone.monitor_temperature(temp); self.logs.append(temp)
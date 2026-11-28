from src.exceptions import ColdChainViolationException
class ColdStorageZone:
    def __init__(self, zone_id: str, min_temp: float, max_temp: float):
        self.zone_id, self.min_temp, self.max_temp, self.current_temp = zone_id, min_temp, max_temp, min_temp
    def monitor_temperature(self, temp: float):
        self.current_temp = temp
        if temp < self.min_temp or temp > self.max_temp: raise ColdChainViolationException("Bad temp")
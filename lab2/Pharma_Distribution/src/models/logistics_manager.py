class LogisticsManager:
    def __init__(self, name: str):
        self.name = name
        self.shipments = []
    def assign_shipment(self, shipment):
        self.shipments.append(shipment)
class Shipment:
    def __init__(self, order, vehicle, driver, route):
        self.order = order
        self.vehicle = vehicle
        self.driver = driver
        self.route = route
        self.status = "Preparing"
    def dispatch(self):
        self.status = "In Transit"
        self.driver.update_location(self.route.start)
    def deliver(self):
        self.status = "Delivered"
        self.driver.update_location(self.route.end)
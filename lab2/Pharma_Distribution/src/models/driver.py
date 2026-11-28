class Driver:
    def __init__(self, name: str, license: str):
        self.name = name
        self.license = license
        self.location = "Warehouse"
    def update_location(self, loc: str):
        self.location = loc
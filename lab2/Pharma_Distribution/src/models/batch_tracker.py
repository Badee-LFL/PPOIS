class BatchTracker:
    def __init__(self, batch): self.batch, self.location = batch, "Manufacturer"
    def update_location(self, loc: str): self.location = loc
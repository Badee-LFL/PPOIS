class InventoryAnalyzer:
    def __init__(self, warehouse): self.warehouse = warehouse
    def check_low_stock(self, threshold: int):
        if self.warehouse.current_stock < threshold: return "Low Stock Alert"
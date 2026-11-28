from .employee import Employee
class SalesManager(Employee):
    def __init__(self, name: str, target: float):
        super().__init__(name, "Sales", 5000.0)
        self.target = target
        self.sales = 0.0
    def record_sale(self, amount: float):
        self.sales += amount
    def calculate_commission(self) -> float:
        return self.sales * 0.05
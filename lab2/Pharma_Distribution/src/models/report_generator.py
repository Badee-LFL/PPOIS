from .report import Report
class ReportGenerator:
    def __init__(self): self.reports = []
    def generate_sales_report(self, manager):
        r = Report("Sales", {"manager": manager.name, "sales": manager.sales}); self.reports.append(r)
        return r
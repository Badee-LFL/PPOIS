class Company:
    def __init__(self, name: str, tax_id: str): self.name, self.tax_id, self.departments = name, tax_id, []
    def add_department(self, dept): self.departments.append(dept)
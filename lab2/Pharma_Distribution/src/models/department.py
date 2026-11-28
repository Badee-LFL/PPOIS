class Department:
    def __init__(self, name: str): self.name, self.employees = name, []
    def hire_employee(self, emp): self.employees.append(emp)
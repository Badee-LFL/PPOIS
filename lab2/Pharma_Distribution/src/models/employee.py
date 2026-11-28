class Employee:
    def __init__(self, name: str, role: str, salary: float):
        self.name = name
        self.role = role
        self.salary = salary
    def give_raise(self, percent: float):
        self.salary += self.salary * (percent / 100)
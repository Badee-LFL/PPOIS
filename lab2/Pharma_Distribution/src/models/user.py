class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    def update_name(self, new_name: str):
        self.name = new_name
class Report:
    def __init__(self, title: str, data: dict): self.title, self.data = title, data
    def format_json(self) -> str: return f'{{"title": "{self.title}", "data": {self.data}}}'
class Complaint:
    def __init__(self, client, text: str): self.client, self.text, self.is_resolved = client, text, False
    def resolve(self): self.is_resolved = True
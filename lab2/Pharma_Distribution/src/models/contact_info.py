class ContactInfo:
    def __init__(self, email: str, phone: str): self.email, self.phone = email, phone
    def update_email(self, new_email: str): self.email = new_email
class NotificationService:
    def __init__(self): self.messages = []
    def send_email(self, email: str, msg: str): self.messages.append(f"To {email}: {msg}")
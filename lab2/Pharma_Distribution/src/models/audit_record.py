class AuditRecord:
    def __init__(self, auditor: str, date: str): self.auditor, self.date, self.findings = auditor, date, []
    def log_finding(self, f: str): self.findings.append(f)
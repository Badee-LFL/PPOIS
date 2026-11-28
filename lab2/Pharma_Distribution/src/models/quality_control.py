class QualityControl:
    def __init__(self, inspector: str): self.inspector, self.tests_passed = inspector, 0
    def run_test(self, passed: bool):
        if passed: self.tests_passed += 1
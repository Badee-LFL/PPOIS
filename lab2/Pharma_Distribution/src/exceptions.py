class PharmaException(Exception):
    """Base exception for all pharma-related errors."""

class InsufficientStockException(PharmaException):
    pass

class InvalidMedicineDataException(PharmaException):
    pass

class ExpiredBatchException(PharmaException):
    pass

class PrescriptionRequiredException(PharmaException):
    pass

class OrderNotFoundException(PharmaException):
    pass

class InvalidOrderStateException(PharmaException):
    pass

class SupplierNotApprovedException(PharmaException):
    pass

class ColdChainViolationException(PharmaException):
    pass

class InvalidClientDataException(PharmaException):
    pass

class DuplicateMedicineException(PharmaException):
    pass

class PaymentFailedException(PharmaException):
    pass

class WarehouseCapacityException(PharmaException):
    pass
class PlatformException(Exception):
    pass

class CourseNotFoundException(PlatformException):
    pass

class AlreadyEnrolledException(PlatformException):
    pass

class PaymentFailedException(PlatformException):
    pass

class InvalidSubmissionException(PlatformException):
    pass

class AccessDeniedException(PlatformException):
    pass

class QuizAlreadyAttemptedException(PlatformException):
    pass

class InstructorNotApprovedException(PlatformException):
    pass

class ContentRejectedException(PlatformException):
    pass

class ScheduleConflictException(PlatformException):
    pass

class CertificateNotEligibleException(PlatformException):
    pass

class RefundNotAllowedException(PlatformException):
    pass

class PlagiarismDetectedException(PlatformException):
    pass

class PlatformMaintenanceException(PlatformException):
    pass
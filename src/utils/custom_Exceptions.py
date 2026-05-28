class AppException(Exception):

    status_code = 500
    msg = "Internal Server Error"

    def __init__(self, msg=None):

        if msg:
            self.msg = msg
        super().__init__(self.msg)


class BadRequestException(AppException):

    status_code = 400
    msg = "Bad Request"


class NotFoundException(AppException):

    status_code = 404
    msg = "Resource Not Found"


class UnauthorizedException(AppException):

    status_code = 401
    msg = "Unauthorized"


class ForbiddenException(AppException):

    status_code = 403
    msg = "Forbidden"

class EnrollmentNotFound(NotFoundException):

    msg = "Enrollment not found"


class DocumentAlreadyExists(BadRequestException):

    msg = "Document already exists"


class DocumentUploadfailed(BadRequestException):

    msg = "Cannot upload document in future cycle"

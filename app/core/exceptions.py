from fastapi import HTTPException

from app.core.constants import (
    INSUFFICIENT_PERMISSIONS_FOR_ACTION,
    INSUFFICIENT_PERMISSIONS_FOR_FIELD,
    NOT_EXIST_EXCEPTION_MESSAGE,
    NOT_EXIST_BY_USER_ID_EXCEPTION_MESSAGE
)


class CRUDNotFoundByUserIDException(HTTPException):
    def __init__(self, model, user_id):
        super().__init__(
            status_code=404,
            detail=NOT_EXIST_BY_USER_ID_EXCEPTION_MESSAGE.format(
                model=model.table_name(), user_id=user_id),
        )


class CRUDNotFoundException(HTTPException):
    def __init__(self, model, pk):
        super().__init__(
            status_code=404,
            detail=NOT_EXIST_EXCEPTION_MESSAGE.format(
                model=model.table_name(), id=pk),
        )


class EndpointFieldForbiddenException(HTTPException):
    def __init__(self, field):
        super().__init__(
            status_code=403,
            detail=INSUFFICIENT_PERMISSIONS_FOR_FIELD.format(field=field),
        )


class NoAccessByUserException(HTTPException):
    def __init__(self, email):
        super().__init__(
            status_code=403,
            detail=INSUFFICIENT_PERMISSIONS_FOR_ACTION.format(email=email),
        )

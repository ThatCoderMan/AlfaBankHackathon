from fastapi import HTTPException

from app.core import constants


class NotExistException(HTTPException):
    def __init__(self, model, pk=None):
        super().__init__(
            status_code=404,
            detail=(
                constants.NOT_EXIST_ID_MESSAGE.format(name=str(model), id=pk)
                if pk is not None
                else constants.NOT_EXIST_MESSAGE.format(name=str(model))
            ),
        )


class NoAccessActionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403, detail=constants.NO_ACCESS_ACTION_MESSAGE
        )


class NoAccessFieldException(HTTPException):
    def __init__(self, field):
        super().__init__(
            status_code=403,
            detail=constants.NO_ACCESS_FIELD_MESSAGE.format(field=field),
        )


class NoAccessObjectException(HTTPException):
    def __init__(self, model):
        super().__init__(
            status_code=403,
            detail=constants.NO_ACCESS_OBJECT_MESSAGE.format(name=str(model)),
        )


class UnacceptableStatusException(HTTPException):
    def __init__(self, status_id):
        super().__init__(
            status_code=401,
            detail=constants.UNACCEPTABLE_STATUS_MESSAGE.format(
                status_id=status_id),
        )

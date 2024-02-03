from fastapi import HTTPException
from pydantic import BaseModel

from app.core import constants


class ErrorDetail(BaseModel):
    loc: list[str]
    msg: str
    type: str


class Error403Schema(BaseModel):
    detail: list[ErrorDetail]


class ErrorSchema(BaseModel):
    detail: str


class NotExistException(HTTPException):
    def __init__(self, model, pk=None):
        super().__init__(
            status_code=404,
            detail=(
                constants.NOT_EXIST_ID_MESSAGE.format(
                    name=model.__str__(), id=pk
                )
                if pk is not None
                else constants.NOT_EXIST_MESSAGE.format(name=model.__str__())
            ),
        )


class NoAccessActionException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=403,
            detail=[
                {
                    'loc': ["body"],
                    'msg': constants.NO_ACCESS_ACTION_MESSAGE,
                    'type': "no_access_action",
                }
            ],
        )


class NoAccessFieldException(HTTPException):
    def __init__(self, field):
        super().__init__(
            status_code=403,
            detail=[
                {
                    'loc': ["body", field],
                    'msg': constants.NO_ACCESS_FIELD_MESSAGE.format(
                        field=field
                    ),
                    'type': "no_access_field",
                }
            ],
        )

    class NoAccessObjectException(HTTPException):
        def __init__(self, model):
            super().__init__(
                status_code=403,
                detail=[
                    {
                        'loc': ["body", model.__str__()],
                        'msg': constants.NO_ACCESS_OBJECT_MESSAGE.format(
                            name=model.__str__()
                        ),
                        'type': "no_access_object",
                    }
                ],
            )

    class UnacceptableStatusException(HTTPException):
        def __init__(self, status_id):
            super().__init__(
                status_code=403,
                detail=[
                    {
                        'loc': ["body", 'status_id'],
                        'msg': constants.UNACCEPTABLE_STATUS_MESSAGE.format(
                            status_id=status_id
                        ),
                        'type': "unacceptable_status",
                    }
                ],
            )

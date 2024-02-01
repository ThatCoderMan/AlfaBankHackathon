from fastapi import HTTPException

from app.core.constants import NOT_EXIST_EXCEPTION


class CRUDNotFoundException(HTTPException):
    def __init__(self, model, pk):
        super().__init__(status_code=404,
                         detail=NOT_EXIST_EXCEPTION.format(model=model, id=pk))

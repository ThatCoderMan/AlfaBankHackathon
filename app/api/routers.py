from api.endpoints import employees_router, idp_router
from fastapi import APIRouter

main_router = APIRouter()
main_router.include_router(
    employees_router, prefix="/api/v1/employees", tags=["Сотрудники"]
)
main_router.include_router(idp_router, prefix="/api/v1/pdp", tags=["ИПР"])

from fastapi import APIRouter

from app.api.v1.endpoints import (
    employee_router,
    pdp_router,
    task_properties_router,
    task_router,
    template_properties_router,
    template_router,
)

router = APIRouter()

router.include_router(employee_router, tags=["Employees"])
router.include_router(pdp_router, prefix="/pdp", tags=["PDPs"])
router.include_router(task_router, prefix="/task", tags=["Tasks"])
router.include_router(template_router, prefix="/template", tags=["Templates"])
router.include_router(
    task_properties_router, prefix='/task_properties', tags=["Task Properties"]
)
router.include_router(
    template_properties_router,
    prefix='/template_properties',
    tags=["Template Properties"],
)

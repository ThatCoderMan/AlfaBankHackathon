from sqlalchemy.ext.asyncio import AsyncSession

from app.core import exceptions
from app.core.constants import NOT_STATED_ID, PLANED_STATUS_ID
from app.crud import pdp_crud, task_crud, template_crud
from app.models import PDP, Task, Template, User


async def create_tasks_from_template(
    session: AsyncSession, template_id: int, users_ids: set[int]
):
    template_obj = await template_crud.get(
        template_id=template_id, session=session
    )
    if template_obj is None:
        raise exceptions.NotExistException(model=Template, pk=template_id)
    pdps = await pdp_crud.get_multi_by_users(session, users_ids)
    if not pdps:
        raise exceptions.NotExistException(model=PDP)
    task_dict = {
        field: value
        for field, value in template_obj.__dict__.items()
        if hasattr(Task, field) and field not in ['id', 'type']
    }
    task_dict['status_id'] = PLANED_STATUS_ID
    tasks_data = []
    for pdp in pdps:
        task_data = {'pdp_id': pdp}
        task_data.update(task_dict)
        tasks_data.append(task_data)
    await task_crud.create_multi_from_dict(session=session, data=tasks_data)
    return True


async def create_template_from_task(
    session: AsyncSession, task_id: int, user: User
):
    task_obj = await task_crud.get(task_id=task_id, session=session)
    if task_obj is None:
        raise exceptions.NotExistException(model=Task, pk=task_id)
    template_data = {
        field: value
        for field, value in task_obj.__dict__.items()
        if hasattr(Template, field) and field not in ['id', 'type']
    }
    template_data['grade_id'] = NOT_STATED_ID
    template_data['direction_id'] = NOT_STATED_ID
    template_data['user_id'] = user.id
    await template_crud.create_from_dict(session=session, data=template_data)
    return True

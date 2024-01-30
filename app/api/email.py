from sqlalchemy import select, join
from starlette.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

from app.models.user import UserRole, User, user_user
from app.models import PDP

conf = ConnectionConfig(
    MAIL_USERNAME="AlfaBankHackathon@ya.ru",
    MAIL_PASSWORD="yfidmxkvwehwyhju",
    MAIL_FROM="AlfaBankHackathon@ya.ru",
    MAIL_PORT=465,
    MAIL_SERVER="smtp.yandex.ru",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False,
)


async def send_email(email):
    message = MessageSchema(
        subject="AlfaBankHackathon@ya.ru",
        recipients=['AlfaBankHackathon@ya.ru'],  # email.get("email")
        body=email.get('message'),
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200,
                        content={'message': 'email has been sent'})


async def get_email_chief(user, session):
    stmt = select(User).select_from(
        join(user_user, User, user_user.c.chief_id == User.id)
    ).where(user_user.c.user_id == user.id)

    result = await session.execute(stmt)
    return result.scalar_one()


async def get_email_employee(pdp_id, session):
    stmt = select(User.email).select_from(
        join(PDP, User, PDP.user_id == User.id)).where(PDP.id == pdp_id)
    result = await session.execute(stmt)

    return result.scalar()


async def new_post_task(data):
    session = data.get('session')
    user = data.get('user')
    task = data.get('task')

    if user.role == UserRole.CHIEF and task.status.value != 'Запланирована':
        email_employee = await get_email_employee(task.pdp_id, session)

        message = f'У вас новая задача со статусом "{task.status.value}"'
        data_email = {
            'email': email_employee,
            'message': message
        }

        await send_email(data_email)

    elif user.role == UserRole.EMPLOYEE:
        message_chief = f'Сотрудник {user.email} подал заявку на развитие.'

        email_chief = await get_email_chief(user, session)

        data_email_chief = {
            'email': email_chief.email,
            'message': message_chief
        }
        await send_email(data_email_chief)


async def change_task_email(data):
    user = data.get('user')
    old_status = data.get('old_status')
    task = data.get('task')
    new_status = task.status.value
    old_chief_comment = data.get('old_chief_comment')
    old_employee_comment = data.get('old_employee_comment')
    new_employee_comment = task.employee_comment
    new_chief_comment = task.chief_comment
    session = data.get('session')

    if user.role == UserRole.CHIEF:
        email_employee = await get_email_employee(task.pdp_id, session)

        if new_status != old_status and old_chief_comment != new_chief_comment:
            message = (f'Статус задачи в Вашем Индивидуальном плане развития '
                       f'"{task.title}" изменен руководителем '
                       f'с "{old_status}" на "{new_status}" '
                       f'и добавлен комментарий')
            data_email_employee = {
                'email': email_employee,
                'message': message
            }

            await send_email(data_email_employee)

        elif new_status != old_status:
            message = (f'Статус задачи в Вашем Индивидуальном плане развития '
                       f'"{task.title}" изменен руководителем '
                       f'с "{old_status}" на "{new_status}"')
            data_email_employee = {
                'email': email_employee,
                'message': message
            }

            await send_email(data_email_employee)

        elif old_chief_comment != new_chief_comment:
            message = (f'Руководитель оставил новый комментарий к задаче '
                       f'"{task.title}".')
            data_email_employee = {
                'email': email_employee,
                'message': message
            }

            await send_email(data_email_employee)

    if user.role == UserRole.EMPLOYEE:

        email_chief = await get_email_chief(user, session)

        if (new_status != old_status and
                old_employee_comment != new_employee_comment):
            message = (f'Изменен статус заявки "{task.title}" '
                       f'с "{old_status}" на "{new_status}" '
                       f'и добавлен комментарий')
            data_email_chief = {
                'email': email_chief.email,
                'message': message
            }

            await send_email(data_email_chief)

        elif new_status != old_status:
            message = (f'Сотрудник {user.email} изменил статус задачи '
                       f'с "{old_status}" на "{new_status}"')
            data_email_chief = {
                'email': email_chief,
                'message': message
            }

            await send_email(data_email_chief)

        elif old_employee_comment != new_employee_comment:
            message = (f'Сотрудник {user.email} добавил комментарий к задаче '
                       f'"{task.title}"')
            data_email_chief = {
                'email': email_chief,
                'message': message
            }

            await send_email(data_email_chief)

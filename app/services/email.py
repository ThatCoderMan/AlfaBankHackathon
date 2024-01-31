from fastapi import HTTPException, status
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from starlette.responses import JSONResponse

from app.core import constants
from app.core.config import settings
from app.core.db import AsyncSessionLocal
from app.crud import user_crud
from app.models.user import UserRole

conf = ConnectionConfig(
    MAIL_USERNAME=settings.mail_username,
    MAIL_PASSWORD=settings.mail_password,
    MAIL_FROM=settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_STARTTLS=settings.mail_starttls,
    MAIL_SSL_TLS=settings.mail_ssl_tls,
    USE_CREDENTIALS=settings.use_credentials,
    VALIDATE_CERTS=settings.validate_certs,
)


async def send_email(email, message_in):
    message = MessageSchema(
        subject="AlfaBankHackathon",
        recipients=[email],
        body=message_in,
        subtype=MessageType.html,
    )

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        return JSONResponse(
            status_code=200, content={'message': 'Email был отправлен'}
        )
    except Exception as exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Ошибка отправки email : {str(exception)}',
        )


async def new_post_task(data):
    user = data.get('user')
    task = data.get('task')

    if user.role == UserRole.CHIEF and task.status.value != 'Запланирована':
        async with AsyncSessionLocal() as async_session:
            email_employee = await user_crud.get_email_employee(
                user=user, session=async_session
            )

        message = constants.EMPLOYEE_NEW_POST_MESSAGE.format(
            first_name=email_employee.first_name,
            last_name=email_employee.last_name,
            task_title=task.title,
            status_value=task.status.value,
            first_chief=user.first_name,
            last_chief=user.last_name,
            email_chief=user.email,
        )

        await send_email(email_employee.email, message)

    elif user.role == UserRole.EMPLOYEE:
        async with AsyncSessionLocal() as async_session:
            email_chief = await user_crud.get_email_chief(
                user=user, session=async_session
            )
        message = constants.CHEIF_NEW_POST_MESSAGE.format(
            first_name=email_chief.first_name,
            last_name=email_chief.last_name,
            first_employee=user.first_name,
            last_employee=user.last_name,
            email_employee=user.email,
        )

        await send_email(email_chief.email, message)


async def change_task_email(data):
    user = data.get('user')
    old_status = data.get('old_status')
    task = data.get('task')
    new_status = task.status.value
    old_chief_comment = data.get('old_chief_comment')
    old_employee_comment = data.get('old_employee_comment')
    new_employee_comment = task.employee_comment
    new_chief_comment = task.chief_comment

    if user.role == UserRole.CHIEF:
        async with AsyncSessionLocal() as async_session:
            email_employee = await user_crud.get_email_employee(
                user=user, session=async_session
            )

        if new_status != old_status and old_chief_comment != new_chief_comment:
            message = (
                constants.EMPLOYEE_NEW_PATH_MESSAGE_COMMENT_STATUS.format(
                    first_name=email_employee.first_name,
                    last_name=email_employee.last_name,
                    task_title=task.title,
                    chief_first=user.first_name,
                    chief_last=user.last_name,
                    old_status=old_status,
                    new_status=new_status,
                    email_chief=user.email,
                )
            )

            await send_email(email_employee.email, message)

        elif new_status != old_status:
            message = constants.EMPLOYEE_NEW_PATH_MESSAGE_STATUS.format(
                first_name=email_employee.first_name,
                last_name=email_employee.last_name,
                task_title=task.title,
                chief_first=user.first_name,
                chief_last=user.last_name,
                old_status=old_status,
                new_status=new_status,
                email_chief=user.email,
            )

            await send_email(email_employee.email, message)

        elif old_chief_comment != new_chief_comment:
            message = constants.EMPLOYEE_NEW_PATH_MESSAGE_COMMENT.format(
                first_name=email_employee.first_name,
                last_name=email_employee.last_name,
                task_title=task.title,
                email_chief=user.email,
            )

            await send_email(email_employee.email, message)

    if user.role == UserRole.EMPLOYEE:
        async with AsyncSessionLocal() as async_session:
            email_chief = await user_crud.get_email_chief(
                user=user, session=async_session
            )

        if (
            new_status != old_status
            and old_employee_comment != new_employee_comment
        ):
            message = constants.CHEIF_NEW_PATH_MESSAGE_COMMENT_STATUS.format(
                first_name=email_chief.first_name,
                last_name=email_chief.last_name,
                task_title=task.title,
                first_employee=user.first_name,
                last_employee=user.last_name,
                old_status=old_status,
                new_status=new_status,
                email_employee=user.email,
            )

            await send_email(email_chief.email, message)

        elif new_status != old_status:
            message = constants.CHEIF_NEW_PATH_MESSAGE_STATUS.format(
                first_name=email_chief.first_name,
                last_name=email_chief.last_name,
                task_title=task.title,
                first_employee=user.first_name,
                last_employee=user.last_name,
                old_status=old_status,
                new_status=new_status,
                email_employee=user.email,
            )

            await send_email(email_chief.email, message)

        elif old_employee_comment != new_employee_comment:
            message = constants.CHEIF_NEW_PATH_MESSAGE_COMMENT.format(
                first_name=email_chief.first_name,
                last_name=email_chief.last_name,
                task_title=task.title,
                first_employee=user.first_name,
                last_employee=user.last_name,
                email_employee=user.email,
            )

            await send_email(email_chief.email, message)

from datetime import datetime, timedelta


"""Константы"""
LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255
LENGTH_LIMITS_USER_FIELDS = 150
LENGTH_LIMITS_LINK_FIELDS = 200
LENGTH_LIMITS_VALUE_FIELDS = 50
LENTH_LIMITS_SKILL_FIELDS = 30

"""Исключения"""
INSUFFICIENT_PERMISSIONS_FOR_ACTION = (
    'У пользователя {email} Недостаточно прав для выполнения действия'
)
INSUFFICIENT_PERMISSIONS_FOR_FIELD = (
    'Недостаточно прав для редактирования поля {field}'
)
NOT_EXIST_EXCEPTION_MESSAGE = 'Объект {model} c id {id} не найден'
NOT_EXIST_BY_USER_ID_EXCEPTION_MESSAGE = 'У пользователя {user_id} нет {model}'

"""Наборы полей"""
CHIEF_TASK_CREATE_FIELDS = (
    'type_id',
    'pdp_id',
    'status_id',
    'title',
    'description',
    'skills',
    'link',
    'chief_comment',
    'starting_date',
    'deadline',
)
CHIEF_TASK_UPDATE_FIELDS = (
    'type_id',
    'status_id',
    'title',
    'description',
    'skills',
    'link',
    'chief_comment',
    'starting_date',
    'deadline',
)
EMPLOYEE_TASK_CREATE_FIELDS = (
    'title',
    'description',
    'employee_comment',
    'starting_date',
    'deadline'
)
EMPLOYEE_TASK_UPDATE_FIELDS = ('employee_comment', 'status_id')

"""Схемы для swagger"""
TASK_CREATE_EXAMPLES = {
    'for chief': {
        'summary': 'Chief request example',
        'description': 'Fields for chief request',
        'value': {
            'type_id': 1,
            'pdp_id': 1,
            'status_id': 1,
            'title': 'string',
            'description': 'string',
            'skills': ['skill_1',],
            'link': 'string',
            'chief_comment': 'string',
            'starting_date': datetime.today().date(),
            'deadline': datetime.today().date() + timedelta(days=10),
        }
    },
    'for employee': {
        'summary': 'Employee request example',
        'description': 'Fields for employee request',
        'value': {
            'title': 'string',
            'description': 'string',
            'employee_comment': 'string',
            'starting_date': datetime.today().date(),
            'deadline': datetime.today().date() + timedelta(days=10),
        }
    }}
TASK_UPDATE_EXAMPLES = {
    'for chief': {
        'summary': 'Chief request example',
        'description': 'Fields for chief request',
        'value': {
            'type_id': 1,
            'status_id': 1,
            'title': 'string',
            'description': 'string',
            'skills': ['skill_1',],
            'link': 'string',
            'chief_comment': '',
            'starting_date': datetime.today().date(),
            'deadline': datetime.today().date() + timedelta(days=10),
        }
    },
    'for employee': {
        'summary': 'Employee request example',
        'description': 'Fields for employee request',
        'value': {
            'status_id': 1,
            'employee_comment': 'string',
        }
    }}

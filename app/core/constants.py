from datetime import datetime, timedelta

# Constants
LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255
LENGTH_LIMITS_USER_FIELDS = 150
LENGTH_LIMITS_LINK_FIELDS = 200
LENGTH_LIMITS_VALUE_FIELDS = 50
LENGTH_LIMITS_SKILL_FIELDS = 30


# Exception messages
NO_ACCESS_ACTION_MESSAGE = 'No access to execute the action.'
NO_ACCESS_FIELD_MESSAGE = 'No access to field {field}.'
NO_ACCESS_OBJECT_MESSAGE = 'No access to {name}.'
NOT_EXIST_ID_MESSAGE = '{name} with id {id} does not exist.'
NOT_EXIST_MESSAGE = '{name} does not exist.'


# Schema access fields
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
    'deadline',
)
EMPLOYEE_TASK_UPDATE_FIELDS = ('employee_comment', 'status_id')


# Swagger schemas
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
            'skills': ['string'],
            'link': 'string',
            'chief_comment': 'string',
            'starting_date': datetime.today().date(),
            'deadline': datetime.today().date() + timedelta(days=10),
        },
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
        },
    },
}
TASK_UPDATE_EXAMPLES = {
    'for chief': {
        'summary': 'Chief request example',
        'description': 'Fields for chief request',
        'value': {
            'type_id': 1,
            'status_id': 1,
            'title': 'string',
            'description': 'string',
            'skills': ['string'],
            'link': 'string',
            'chief_comment': 'string',
            'starting_date': datetime.today().date(),
            'deadline': datetime.today().date() + timedelta(days=10),
        },
    },
    'for employee': {
        'summary': 'Employee request example',
        'description': 'Fields for employee request',
        'value': {
            'status_id': 1,
            'employee_comment': 'string',
        },
    },
}

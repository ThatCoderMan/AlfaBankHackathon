LENGTH_LIMITS_STRING_FIELDS = 100
LENGTH_LIMITS_TEXT_FIELDS = 255
LENGTH_LIMITS_USER_FIELDS = 150
LENGTH_LIMITS_LINK_FIELDS = 200
LENGTH_LIMITS_VALUE_FIELDS = 50
LENTH_LIMITS_SKILL_FIELDS = 30

EMPLOYEE_NEW_POST_MESSAGE = (
    'Добрый день, {first_name} {last_name}!<br>'
    'У вас новая задача "{task_title}" со статусом "{status_value}".<br>'
    '<br>С уважением, {first_chief} {last_chief}.<br>'
    'Контактные данные: {email_chief}'
)

CHEIF_NEW_POST_MESSAGE = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Сотрудник {first_employee} {last_employee} подал заявку на развитие.<br>'
    '<br>Контактные данные: {email_employee}<br>'
)

EMPLOYEE_NEW_PATH_MESSAGE_COMMENT_STATUS = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Статус задачи "{task_title}" в Вашем Индивидуальном плане развития '
    'был изменен руководителем {chief_first} {chief_last} со статуса '
    '"{old_status}" на статус "{new_status}", '
    'а также добавлен комментарий.<br>'
    '<br>Контактные данные: {email_chief}<br>'
)

EMPLOYEE_NEW_PATH_MESSAGE_STATUS = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Статус задачи "{task_title}" в Вашем Индивидуальном плане развития '
    'был изменен руководителем {chief_first} {chief_last} со статуса '
    '"{old_status}" на статус "{new_status}". <br>'
    '<br>Контактные данные: {email_chief}<br>'
)

EMPLOYEE_NEW_PATH_MESSAGE_COMMENT = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Руководитель оставил новый комментарий к задаче "{task_title}". <br>'
    '<br>Контактные данные: {email_chief}<br>'
)

CHEIF_NEW_PATH_MESSAGE_COMMENT_STATUS = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Сотрудник {first_employee} {last_employee}.'
    'изменил статус задачи "{task_title}" с "{old_status}" на "{new_status}" '
    'и добавил комментарий<br>'
    '<br>Контактные данные: {email_employee}<br>'
)

CHEIF_NEW_PATH_MESSAGE_STATUS = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Сотрудник {first_employee} {last_employee} изменил статус задачи '
    '"{task_title}" с "{old_status}" на "{new_status}"<br>'
    '<br>Контактные данные: {email_employee}<br>'
)

CHEIF_NEW_PATH_MESSAGE_COMMENT = (
    'Добрый день, {first_name} {last_name}!<br>'
    'Сотрудник {first_employee} {last_employee} добавил комментарий к задаче '
    '"{task_title}"<br>'
    '<br>Контактные данные: {email_employee}<br>'
)

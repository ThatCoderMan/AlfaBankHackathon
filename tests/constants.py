from datetime import datetime
from urllib.parse import urlparse

directions = ['не определен', 'Дизайн', 'Delivery Менеджмент', 'ВА аналитика',
              'SA аналитика', 'Программирование', 'Discovery менеджмент',
              'Soft Skills', 'Маркетинг']
grade = ['не определен', 'Junior', 'Middle', 'Senior']

skill = ['волшебник', 'маг', 'мечтатель']

types = ['Иное', 'Внутренний курс', 'Внешний курс', 'Менторство',
         'Наставничество', 'Самостоятельное обучение']

status = ['В работе', 'Выполнена', 'Отменена', 'Запланирована', 'Исполнена',
          'Заявка']
roles = ['CHIEF', 'CHIEF', 'CHIEF', 'CHIEF', 'EMPLOYEE', 'EMPLOYEE']

users_data = ['chief@email.com CHIEF Ecologist',
              'employee@email.com EMPLOYEE Technologist',
              'another@email.com EMPLOYEE Pacifist']

exp_types_common = {'id': int, 'value': str, }

exp_types_task = {'title': str, 'starting_date': str,
                  'deadline': str, 'id': int, 'pdp_id': int,
                  'type': dict,
                  'status': dict,
                  'description': str,
                  'skills': list,
                  'link': str,
                  'chief_comment': str,
                  }

task_data = {
    'title': "Тест_Title",
    'starting_date': "2024-02-01",
    'deadline': "2025-02-01",
    'type_id': 1,
    'pdp_id': 2,
    'status_id': 1,
    'description': 'Описание Задачи',
    'skills': ['волшебник'],
    'link': 'http://task_link',
    'chief_comment': '',
    'employee_comment': ''
}

task_data_employee = {
    'title': "Тест_Title_Employee",
    'starting_date': "2024-02-01",
    'deadline': "2025-02-01",
    'type_id': 2,
    'pdp_id': 1,
    'description': 'Описание Задачи_Employee',
    'employee_comment': ''
}

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
              'employee@email.com EMPLOYEE Technologist']

exp_types_common = {'id': int, 'value': str, }

exp_types_task = {'title': str, 'starting_date': datetime,
                  'deadline': datetime, 'id': int, 'pdp_id': int,
                  'type': dict,
                  'status': dict,
                  'description': str,
                  'skills': list,
                  'link': urlparse,
                  'chief_comment': str,
                  'employee_comment': str}

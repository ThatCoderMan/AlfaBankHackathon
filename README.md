<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Alfa-Bank.svg" alt="AlfaBankHackathon">
</p>

<div id="header" align="center">
  <img src="https://img.shields.io/badge/Python-3.11.1-F8F8FF?style=for-the-badge&logo=python&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/FastAPI-0.109.1-F8F8FF?style=for-the-badge&logo=FastAPI&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=F5F5DC">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.23-F8F8FF?style=for-the-badge&logo=SQLAlchemy&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Pydantic-2.1.0-F8F8FF?style=for-the-badge&logo=pydantic&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Uvicorn-0.26.0-F8F8FF?style=for-the-badge&logo=uvicorn&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Alembic-1.13.1-F8F8FF?style=for-the-badge&logo=alembic&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
</div>

<br>
<br>
<br>

Документация к API будет доступна по url-адресу [AlfaBankHackathon/SWAGER](http://alfabankhack.ddns.net:8000/docs)

Ссылка на zip-архив с некоторыми скриншотами [zip](https://drive.google.com/file/d/1bScOyVM6yZnohbRz4_n6zsYUs8QWWmuV/view?usp=drive_link)

<details><summary><h1>Сервис по развитию сотрудников</h1></summary>

* **MVP:**
  + Цель: Организация работы по развитию сотрудников IT-департамента в рамках Индивидуального плана развития (ИПР).
  + Размещение: Внутри корпоративного портала Альфа-банка "Alfa People".


* **Функциональные возможности:**
  + Создание и управление ИПР.
  + Постановка целей и задач.
  + Планирование сроков выполнения.
  + Отслеживание выполнения задач.

* **Обучение:**
  + Отслеживание прогресса обучения.
  + Получение обратной связи.
  + Аналитика по ИПР.
  + Систематизация работы по развитию сотрудников.

* **Преимущества:**
  + Индивидуальные планы развития для каждого сотрудника.
  + Отслеживание прогресса развития.
  + Автоматизация рутинных процессов.

* **Целевая аудитория:**
  + Сотрудники IT-департамента Альфа-банка.
  + Руководители IT-департамента.



</details>


<details><summary><h1>Инструкция по установке</h1></summary>

Клонируйте репозиторий и перейдите в него.
```bash
git@github.com:ThatCoderMan/AlfaBankHackathon.git
```

Для установки виртуального окружения с помощью **Poetry** нужно установить его через pip:
```bash
pip install poetry
```
Для активации poetry нужно прописать:
```bash
poetry install
```

### Работа с зависимостями
Обновления зависимостей (при загрузки обновлений репозитория с GitHub):
```bash
poetry update
```
Создайте файл **.env**, в корневой папке проекта, с переменными окружения.

  ```
  APP_TITLE=AlfaBankHackathon
  DESCRIPTION=AlfaBankHackathon
  SECRET=SECRET
  DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
  
  MAIL_USERNAME=your_username
  MAIL_PASSWORD=mail_password
  MAIL_FROM=example@mail.com
  MAIL_PORT=465
  MAIL_SERVER=smtp
  ```


Находясь в корневой папке проекта выполните миграции.
  ```
  alembic revision --autogenerate -m "Initial migration"
  alembic upgrade head
  ```

Для запуска сервера используйте данную команду:
  ```
  uvicorn app.main:app --reload
  ```

</details>

<details><summary><h1>Запуск проекта через докер</h1></summary>

- Клонируйте репозиторий.
- Перейдите в папку **infra** и создайте в ней файл **.env** с переменными окружения:
    ```
  DB_NAME=postgres
  POSTGRES_USER=postgres
  DB_HOST=db
  DB_PORT=5432
  POSTGRES_PASSWORD=password
  CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
  PGADMIN_DEFAULT_EMAIL=user@gmail.ru
  PGADMIN_DEFAULT_PASSWORD=user_password
    ``` 
- Из папки **infra** запустите docker-compose-prod.yaml:
  ```
  ~$ docker-compose up -d --build
  ```
- В контейнере **backend** выполните миграции:
  ```
  ~$ docker-compose exec backend alembic revision --autogenerate -m "Initial migration"

  ~$ docker-compose exec backend alembic upgrade head
  ```

Документация к API будет доступна по url-адресу [127.0.0.1/redoc](http://127.0.0.1/redoc)

</details>

<details><summary>Ссылки на используемые библиотеки</summary>
    
- [Python](https://www.python.org/downloads/release/python-3111/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Uvicorn](https://www.uvicorn.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [Docker](https://www.docker.com/)

</details>

* **Разработчики Backend:**
  + [Артемий](https://github.com/ThatCoderMan)
  + [Василий](https://github.com/inferno681)
  + [Владислав](https://github.com/VladislavCR)
  + [Сергей](https://github.com/Conqerorior)
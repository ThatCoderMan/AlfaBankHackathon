<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Alfa-Bank.svg" alt="AlfaBankHackathon">
</p>

<div id="header" align="center">
  <h1>«AlfaBankHackathon»</h1>
  <img src="https://img.shields.io/badge/Python-3.11.1-F8F8FF?style=for-the-badge&logo=python&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/FastAPI-0.104.1-F8F8FF?style=for-the-badge&logo=FastAPI&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/PostgreSQL-555555?style=for-the-badge&logo=postgresql&logoColor=F5F5DC">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0.23-F8F8FF?style=for-the-badge&logo=SQLAlchemy&logoColor=20B2AA">
  <img src="https://img.shields.io/badge/Docker-555555?style=for-the-badge&logo=docker&logoColor=2496ED">
</div>

Документация к API будет доступна по url-адресу [AlfaBankHackathon/SWAGER](http://alfabankhack.ddns.net:8000/docs)

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

* **Backend:**
  + [Артемий](https://github.com/ThatCoderMan)
  + [Василий](https://github.com/inferno681)
  + [Владислав](https://github.com/VladislavCR)
  + [Сергей](https://github.com/Conqerorior)

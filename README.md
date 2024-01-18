<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/77/Alfa-Bank.svg" alt="AlfaBankHackathon">
</p>

<h1 align="center">AlfaBankHackathon</h1>

Клонируйте репозиторий и перейдите в него.

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
# AlfaBankHackathon

- Клонируйте репозиторий и перейдите в него.
- Установите и активируйте виртуальное окружение.
- Установите зависимости из файла requirements.txt
    ```
    python -m pip install --upgrade pip
    pip install poetry
    poetry install
    poetry update
    ``` 
- Создайте файл **.env**, в корневой папке проекта, с переменными окружения.
  ```
  DB_NAME=postgres
  POSTGRES_USER=postgres
  DB_HOST=localhost
  DB_PORT=5432
  POSTGRES_PASSWORD=password

  ```
- Находясь в корневой папке проекта выполните миграции.
  ```
  alembic revision --autogenerate -m "Initial migration"
  alembic upgrade head
  ```

- Для запуска сервера используйте данную команду:
  ```
  uvicorn app.main:app --reload
  ```
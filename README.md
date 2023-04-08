(https://github.com/nikinika/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# api_yamdb
### Описание проекта:
Проект представляет собой API для социальной сети оценок фильмов, книг и музыкальных произведений.

### Технологии:
- Python 3.9  
- Django 3.2
- DRF
- Docker
- Postgresql
- Nginx
- Gunicorn

### Как запустить проект:
#### 1. Клонируте репозиторий `$ git clone git@github.com:nikinika/yamdb_final.git`
#### 2. В директории `infra/`, командой `$touch .env`, создайте файл `.env` со следующими переменными
- DJANGO_KEY='ваш secret_key django'
- DB_ENGINE=django.db.backends.postgresql
- DB_NAME= название БД
- POSTGRES_USER= ваше имя пользователя
- POSTGRES_PASSWORD= пароль для доступа к БД
- DB_HOST=db
- DB_PORT=5432
#### 3. В терминале находясь в папке `infra/` выполните комманду
#### `$ docker-compose up -d` или `$ docker-compose up -d --build`
#### если нужно пересобрать контейнеры
#### 4. Создайте файлы миграции `$ docker-compose exec web python manage.py makemigrations`
#### 5. Примените миграции `$ docker-compose exec web python manage.py migrate`
#### 6. Соберите статику `$ docker-compose exec web python manage.py collectstatic --no-input`
#### 7. Для доступа к админке создайте суперюзера `$ docker-compose exec web python manage.py createsuperuser`
#### 8. Чтобы загрузить в базу данные из вашей резевной копии `$ docker-compose exec web python manage.py loaddata fixtures.json`


### Документация по эндпоинтам, запросам и ответам:

http://localhost/redoc/

### Разработчик:
Никитенко Николай 

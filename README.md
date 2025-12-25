# Fitness Club API

RESTful API для управления фитнес-клубом с использованием Django REST Framework.

##  Особенности

- **JWT аутентификация** (токены доступа/обновления)
- **CRUD операции** для всех моделей
- **Пагинация** (10 записей на страницу)
- **Swagger документация** с авторизацией через токен
- **Docker контейнеризация** (PostgreSQL + Django)
- **Готово к интеграции** с React/Vue.js или мобильными приложениями

##  Модели базы данных

1. **Member (Участник)** - информация об участниках клуба
2. **Trainer (Тренер)** - информация о тренерах
3. **Session (Тренировка)** - связывает участников и тренеров

##  Технологии

- Django 4.2.7
- Django REST Framework 3.14.0
- PostgreSQL 15
- JWT аутентификация (djangorestframework-simplejwt)
- Swagger документация (drf-yasg)
- Docker & Docker Compose

## Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/futbik4/Fitness-Club_project.git
cd Fitness-Club_project
```

### 2. Настройка окружения
```bash
cp .env.example .env
# Отредактируйте .env файл при необходимости
```

### 3. Запуск с Docker
```bash
#Запуск
docker-compose up --build
#Остановка
docker-compose down
#Просмотр логов
docker-compose logs web
#Выполнение команд в контейнере 
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 4. Создание суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
## Доступные эндпоинты

- **Swagger UI:** `http://localhost:8000/swagger/`
- **Admin panel:** `http://localhost:8000/admin/`
- **API Root:** `http://localhost:8000/api/`
- **JWT Token:** `http://localhost:8000/api/token/`

## API Endpoints

### Аутентификация
- `POST /api/token/` - Получить JWT токен
- `POST /api/token/refresh/` - Обновить токен

### Участники (members)
- `GET /api/members/` - Список участников
- `POST /api/members/` - Создать участника
- `GET /api/members/{id}/` - Получить участника
- `PUT /api/members/{id}/` - Обновить участника
- `DELETE /api/members/{id}/` - Удалить участника

### Тренеры (trainers)
- `GET /api/trainers/` - Список тренеров
- `POST /api/trainers/` - Создать тренера
- `GET /api/trainers/{id}/` - Получить тренера
- `PUT /api/trainers/{id}/` - Обновить тренера
- `DELETE /api/trainers/{id}/` - Удалить тренера

### Тренировки (sessions)
- `GET /api/workout-sessions/` - Список тренировок
- `POST /api/workout-sessions/` - Создать тренировку
- `GET /api/workout-sessions/{id}/` - Получить тренировку
- `PUT /api/workout-sessions/{id}/` - Обновить тренировку
- `DELETE /api/workout-sessions/{id}/` - Удалить тренировку

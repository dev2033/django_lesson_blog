# Курс по Django - Создание блога

Установка (Для Ubuntu/Debian):

1) Клонируем репозиторий:

    `git clone https://github.com/dev2033/django_lesson_blog.git`

2) Создаем виртуальное окружение:

    `python3 -m venv venv`

3) Активируем его и устанавливаем все зависимости:

    `sourve venv/bin/activate`

    `pip install -r requirements.txt`

4) Делаем миграции:

    `python manage.py migrate`

5) Запускаем проект:

    `python manage.py runserver`

*СТЕК:*

- Python

- Django


Данный проект является уроки по фреймоворку Django. Весь закоментированный код является учебным и не является не нужным.

В корне проекта не забудьте создать папку `media/`

В данном проекте приложение mainapp - является основным, на нем построен весь сайт.

Приложение testapp: 

В нем описан пример **МНОГОУРОВНЕГО МЕНЮ** .

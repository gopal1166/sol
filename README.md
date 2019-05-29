# Session 7 : Django: Getting started

Date: 29/5/2019

install:
    python, 
    django, 
    mod header chrome extension, 
    postman api client


creating django project:

`django-amdin startproject 'project name'`

project folder structure:

```
a folder with same name as project name
init: 
settings: 
    add apps
    database configuration
    static files settings
    middleware settings

urls: (main url config)
    we'll define urls
    we'll include other app's urls

manage: to manage our project: 
        creating apps, 
        creating superuser, 
        migrating the database,
        django shell: django ORM
``

start the development server:
```
$ python manage.py runserver
```

virutalenv: to isolate

instagram:
    python: 3

anotherproject:
    python: 2

virutal environments:

to intall virtualenv: `pip install virtualenv`

to create virtualenv: 'virtualenv -p python3 "venv_name"'

to activate: source venv_name/bin/activate

To check list of packages: `pip freeze`

To create app: `python manage.py startapp "app_name"`

configure in settings.py file in installed_apps

application structure:
```
admin.py: to register models with admin page
models.py: to create tables 
views.py:  to write the logic part

urls.py: to map urls with the views

tests.py: to write test cases
```












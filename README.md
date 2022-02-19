# eClass BackEnd

# Introduction:
This is the back-end app for E-Class system.

## Tools needed
* Git
* Python3 + pip (or any other package manager)

## Setup
* Create virtual environment e.g.: `python -m venv .env`
* Activate virtual environment in console e.g.:
    * `.env/Scripts/activate.ps1` // Windows
    * `source .env/bin/activate` // Linux/Mac
* `pip3 install django` to install django framework,
* `pip3 install djangorestframework` to install django rest framework
* `django-admin startproject dundts_backend` to create **dundts_backend** project,
* `cd dundts_backend` changes directory to the **dundts_backend** project,
* `django-admin startapp eclass` to create eclass api module,
* The tree of the project is as follows:

  ```shell
  ├── db.sqlite3
  ├── dundts_backend
  │   ├── asgi.py
  │   ├── __init__.py
  │   ├── __pycache__
  │   │   ├── __init__.cpython-39.pyc
  │   │   ├── settings.cpython-39.pyc
  │   │   ├── urls.cpython-39.pyc
  │   │   └── wsgi.cpython-39.pyc
  │   ├── settings.py
  │   ├── urls.py
  │   └── wsgi.py
  ├── eclass
  │   ├── admin.py
  │   ├── apps.py
  │   ├── __init__.py
  │   ├── migrations
  │   │   └── __init__.py
  │   ├── models.py
  │   ├── tests.py
  │   └── views.py
  ├── manage.py
  └── README.md
  ```
  
* Adding `'rest_framework',` and `'eclass.apps.EclassConfig',` to the *INSTALLED_APPS* section of *dundts_backend/settings.py*.
Each newly installed app should be added to this section.
* `python3 manage.py runserver` to run the python app.

# eClass BackEnd

# Introduction:
This is the back-end app for E-Class system.

## Tools needed
* Git
* Python3 + pip (or any other package manager)

## Setup and preparation (~ 6 hours)
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

* `pip install pyodbc`
for creating connection to the database.
I had some problems when installing this package, so after some research I found these links helpful:
  * For installing package python3-dev: [Stackoverflow link 1](https://stackoverflow.com/questions/52887357/problems-when-installing-python3-dev)
  * For *Python.h* fatal error: [Stackoverflow link 2](https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory)
* `pip install pandas`

## Creating DAO class and endpoint for getting structural data
To get structural data of e-class tables, a class name **EclassDao** is created 
to maintain all methods needed for getting data from e-class tables and creating structural data.

Endpoint is determined in views.py file of eclass module.

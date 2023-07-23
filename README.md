# Django Documentaion

# Project Installation

Make sure you refer to the django version you are using. A quick way to start a new django project is to run the
following command:

* Install Django:

```shell
pip install django
```

* Install Python Pipenv:

```shell script
pip install pipenv
```

* Go to your desired development folder and create a new django project:

```shell
django-admin startproject Codemonk && cd Codemonk
```

* Install Django on you virtual environment.

```shell
pipenv install django
```

* Install  Requirements

```shell script
pip install requirements.txt
```

* Activate your new virtual environment:

```shell
pipenv shell
```

* create a new django App:

```shell
python manage.py startproject Books
```

* Add Books to INSTALLED_APPS in you new Django Project.

```python
INSTALLED_APPS = [
    ...,
    'Books',
    'rest_framework',
    'django_filters',
    'drf_yasg',
    ...,
]
```

* Perform database migrations:

```shell
python manage.py migrate
```

* Add Django SuperUser and follow the prompts.

```shell
python manage.py createsuperuser
```

* Add URLs to your project's __urls.py__:

```python
from django.urls import include, path

urlpatterns = [
    ...,
    path('book/',include('Api.urls')),,
    ...,
]
```

* Run your project:

```shell
python manage.py runserver
```

* Navigate to Project root view assigned in your project urlpatterns setting (typically http://127.0.0.1:8000/book/api
if you followed this installation guide).
* Use your superuser credentials to login.

# API Documentaion

# API Setup

Official Django REST framework documentation: https://www.django-rest-framework.org/

The Django REST framework is a powerful and flexible toolkit for building web APIs in Django applications. It provides a set of utilities and serializers to easily create RESTful APIs that can handle various data formats, authentication, permissions, and more.

The documentation covers all aspects of DRF, including installation, configuration, serializers, views, authentication, permissions, pagination, versioning, filtering, and more. It's a comprehensive resource that helps developers understand and leverage the features provided by DRF efficiently.

* Install Django REST framework:

```shell
pip install djangorestframework
```

* Add Django REST framework to your Django project:

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'django_filters',
    ...,
]
```

* Configure the DRF API documentation settings:
    In settings.py, configure the DRF API settings to enable the documentation and set the renderer classes for the documentation
```python
REST_FRAMEWORK = {...}
```

* Include your API URLs in the project's URL configuration:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('your_app.urls')),  # Include your app's API URLs
]
```

* Create and configure your app's URL patterns:

```python
# your_app/urls.py

from django.urls import path
from . import views
from rest_framework import routers

urlpatterns = [ ]

router =routers.SimpleRouter()
router.register('api',YOUR_API_VIEW)

urlpatterns+=router.urls

```

* Add API documentation for your views:

```python
from rest_framework import viewsets

class ViewSet(viewsets.ModelViewSet):
    ...
```

* Access the API documentation:
    With the above steps completed, you can now access the API documentation in your browser. Open your web browser and navigate to:

URL :   http://127.0.0.1:8000/api/


Assuming you are running your development server on the default port (8000) and the base URL is set to 'api/' in your project's urls.py file.
You should see an interactive API documentation page showing your API endpoints, their methods (GET, POST, etc.), and the parameters they accept. The browsable API documentation allows you to test your API endpoints directly from the browser, making it convenient for both development and exploration.

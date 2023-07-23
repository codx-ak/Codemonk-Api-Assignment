from django.urls import path
from Books.views import *
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API  Documentation",
      default_version='v1',
      description="API Testing"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

router =routers.SimpleRouter()
router.register('api',BookViewSet)

urlpatterns+=router.urls
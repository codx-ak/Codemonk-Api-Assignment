from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = []

router =routers.SimpleRouter()
router.register('post',PostView)

urlpatterns+=router.urls
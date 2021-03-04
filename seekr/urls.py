from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from seekrapi.views import SeekerProfileViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'seekrs', SeekerProfileViewSet, 'seekr')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

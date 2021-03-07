from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from seekrapi.views import register_user, login_user, SeekerProfileViewSet, LanguagesViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'seekrs', SeekerProfileViewSet, 'seekr')
router.register(r'languages', LanguagesViewSet, 'language')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]

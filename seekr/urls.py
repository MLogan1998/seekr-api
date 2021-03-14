from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from seekrapi.views import register_user, login_user, SeekerProfileViewSet, LanguagesViewSet, SeekerProfileViewSet, EmployerProfileViewSet, UserViewSet, CompanyProfileViewSet, JobPostingViewSet, EmployerActionViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employeraction', EmployerActionViewSet, 'seekr')
router.register(r'seekrs', SeekerProfileViewSet, 'seekr')
router.register(r'languages', LanguagesViewSet, 'language')
router.register(r'profile', SeekerProfileViewSet, 'profile')
router.register(r'employerprofile', EmployerProfileViewSet, 'profile')
router.register(r'company', CompanyProfileViewSet, 'company')
router.register(r'joblisting', JobPostingViewSet, 'company')
router.register(r'user', UserViewSet, 'user')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]

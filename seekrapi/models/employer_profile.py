from django.db import models
from django.conf import settings

def EmployerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default = 1)
    profile_img = models.CharField()  

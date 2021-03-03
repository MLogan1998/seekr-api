from django.db import models
from django.conf import settings
from django.db.models import CASCADE

class EmployerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default=3, on_delete=CASCADE)
    profile_img = models.CharField(max_length=200)  

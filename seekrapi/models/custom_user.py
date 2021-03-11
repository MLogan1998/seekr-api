from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_seeker = models.BooleanField()
    has_profile = models.BooleanField(default=False)
    has_company = models.BooleanField(default=False)
    has_listing = models.BooleanField(default=False)

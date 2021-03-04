from django.db import models
from django.conf import settings
from django.db.models import CASCADE

class SeekerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE, default=1)
    bio = models.TextField(max_length=350)
    profile_img = models.CharField(max_length=200)
    project_name = models.CharField(max_length=200)    
    project_detail = models.TextField(max_length=400)
    project_img = models.CharField(max_length=200)
    github_username = models.CharField(max_length=200)
    tech_ed = models.CharField(max_length=200)
    experience = models.IntegerField()
    work_history = models.CharField(max_length=200, blank=True)
    languages = models.ManyToManyField("Languages", related_name="seeker_languages", related_query_name="seeker_language")

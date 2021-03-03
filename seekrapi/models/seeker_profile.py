from django.db import models
from django.conf import settings

def SeekerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, default = 1)
    bio = models.TextField(max_length=350)
    profile_img = models.CharField()
    project_name = models.CharField()    
    project_detail = models.TextField(max_length=300)
    project_img = models.CharField()
    github_username = models.CharField()
    tech_ed = models.CharField()
    experience = models.IntegerField()
    work_history = models.CharField(blank=True)
    languages = models.ManyToManyField("Languages", related_name="seeker_languages", related_query_name="seeker_language")

from django.db import models
from django.db.models import CASCADE

class SeekerProfile(models.Model):
    user = models.ForeignKey("User", related_name="profiles", related_query_name="profile", on_delete=CASCADE, default=1)
    bio = models.TextField(max_length=350)
    profile_img = models.TextField()
    project_name = models.CharField(max_length=200)    
    project_detail = models.TextField(max_length=400)
    project_img = models.TextField()
    project_url = models.CharField(max_length=200)
    github_username = models.CharField(max_length=200)
    tech_ed = models.CharField(max_length=200)
    languages = models.ManyToManyField("Languages", related_name="seeker_languages", related_query_name="seeker_language")

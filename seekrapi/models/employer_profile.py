from django.db import models
from django.db.models import CASCADE

class EmployerProfile(models.Model):
    user = models.ForeignKey("User", related_name="employerProfiles", related_query_name="EmployerProfile", on_delete=CASCADE, default=1)
    profile_img = models.CharField(max_length=200)  

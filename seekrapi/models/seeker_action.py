from django.db import models
from django.db.models import CASCADE

def SeekerAction(models.Model):
    seeker = models.foreignKey("SeekerProfile", on_delete=CASCADE)
    seeker_response = models.BooleanField()
    job = models.ForeignKey("JobPosting", on_delete=CASCADE)

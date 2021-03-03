from django.db import models
from django.db.models import CASCADE

def EmployerAction(models.Model):
    job = models.ForeignKey("JobPosting", on_delete=CASCADE)
    employer_response = models.BooleanField()
    seeker = models.ForeignKey("SeekerProfile", on_delete=CASCADE)

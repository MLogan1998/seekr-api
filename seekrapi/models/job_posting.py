from django.db import models
from django.db.models import CASCADE

def JobPosting(models.Model):
    employer = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    job_description = models.TextField()
    salary = models.IntegerField()
    benefits = models.BooleanField()

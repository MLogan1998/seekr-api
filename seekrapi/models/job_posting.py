from django.db import models
from django.db.models import CASCADE

class JobPosting(models.Model):
    employer = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    company = models.ForeignKey("CompanyProfile", on_delete=CASCADE)
    job_description = models.TextField()
    salary = models.CharField(max_length=250)
    benefits = models.BooleanField()
    requirements = models.TextField()
    job_title = models.CharField(max_length=250)

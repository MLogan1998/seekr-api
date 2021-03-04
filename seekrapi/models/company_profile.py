from django.db import models
from django.db.models import CASCADE

class CompanyProfile(models.Model):
    employer_profile = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    company_name = models.CharField(max_length=30)
    company_bio = models.TextField()
    company_logo = models.CharField(max_length=200)

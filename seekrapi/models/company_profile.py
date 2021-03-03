from django.db import models
from django.db.models import CASCADE

def CompanyProfile(models.Model):
    employer_profile = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    company_name = models.CharField()
    company_bio = models.TextField()
    company_logo = models.CharField()

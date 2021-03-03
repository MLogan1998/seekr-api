from django.db import models
from django.db.models import CASCADE

def Match(models.Model):
    seeker = models.ForeignKey("SeekerProfile", on_delete=CASCADE)
    employer = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    job = models.ForeignKey("JobPosting", on_delete=CASCADE)

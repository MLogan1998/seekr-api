from django.db import models
from django.db.models import CASCADE

class Match(models.Model):
    seeker = models.ForeignKey("SeekerProfile", null=True, on_delete=CASCADE)
    employer = models.ForeignKey("EmployerProfile", null=True, on_delete=CASCADE)
    job = models.ForeignKey("JobPosting", on_delete=CASCADE)

from django.db import models
from django.db.models import CASCADE

class SeekerAction(models.Model):
    seeker = models.ForeignKey("SeekerProfile", on_delete=CASCADE)
    seeker_response = models.BooleanField()
    job = models.ForeignKey("JobPosting", on_delete=CASCADE)

from django.db import models
from django.db.models import CASCADE

class EmployerAction(models.Model):
    employer = models.ForeignKey("EmployerProfile", on_delete=CASCADE)
    employer_response = models.BooleanField()
    seeker = models.ForeignKey("SeekerProfile", on_delete=CASCADE)

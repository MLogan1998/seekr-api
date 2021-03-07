from django.db  import models

class Languages(models.Model):
    name = models.CharField(max_length=25)
    icon = models.CharField(max_length=25)

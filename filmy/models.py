from django.db import models

class film(models.Model):
    title = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField()
    


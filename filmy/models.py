from django.db import models

class film(models.Model):
    title = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(blank=True, null=True) # nepovinne, proto blank a null
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text='in minutes') # delka filmu
    
    def __str__(self):
        return self.title


from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(blank=True, null=True) # nepovinne, proto blank a null
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text='in minutes') # delka filmu
    main_picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class Actor(models.Model):
    name = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    main_picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    main_picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


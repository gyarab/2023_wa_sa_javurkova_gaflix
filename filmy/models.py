from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField(blank=True, null=True) # nepovinne, proto blank a null
    footage = models.PositiveSmallIntegerField(blank=True, null=True, help_text='in minutes') # delka filmu
    main_picture = models.CharField(max_length=2000, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    # kdyz smazu rezisera tohodle filmu, tak se tenhle atribut nastavi na null
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    # on_delete se v techto pripadech nepouzije, kvuli ManyToMany vazbe, je jich tam nekolik
    actors = models.ManyToManyField('Actor', blank=True, null=True)
    genres = models.ManyToManyField('Genre', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    # vypise vsechny zanry s carkami
    def genres_display(self):
        # rozepsana metoda, kterou jsme pouzili:
        
        # genres = self.genres.all()
        # out = ''
        # for genre in genres:
        #     out += f'[genre.name], '
            
        # return out
        
        return ', '.join(i.name for i in self.genres.all())
    
    
class Actor(models.Model):
    name = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    main_picture = models.CharField(max_length=2000, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    

class Director(models.Model):
    name = models.CharField(max_length=30)
    birth_year = models.PositiveSmallIntegerField(blank=True, null=True)
    main_picture = models.CharField(max_length=2000, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name


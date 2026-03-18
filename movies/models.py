from django.db import models
# Importando do projeto "genres" o model "Genre"
from genres.models import Genre
# Importando do projeto "actors" o model "Actor"
from actors.models import Actor

# Model Movie
class Movie (models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.PROTECT)
    release_date = models.DateField()
    actors = models.ManyToManyField(Actor, related_name='movies')    
    resume = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title
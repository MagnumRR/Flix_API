from django.contrib import admin
# Importando do app movies o model Movie
from movies.models import Movie

# Registrando no Admin Django o acesso ao model Movie
@admin.register(Movie)
class MovieAdmin (admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume')
    
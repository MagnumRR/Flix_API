from django.db import models
# Importar do projeto movies o model Movie
from movies.models import Movie
# Importar do Django, do módulo core, do módulo validators: Max e min
from django.core.validators import MinValueValidator, MaxValueValidator

# Model review
class Review (models.Model):
    movie = models.ForeignKey(Movie, 
            related_name='reviews', 
            on_delete=models.PROTECT
    )
    # Criar uma validação de 0 a 5, utilizando o "validators"
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Message'),
            MaxValueValidator(5, 'Message'),
        ]
    )
    comment = models.TextField(null=True, blank=True)    
    
    # Ajuste para exibir o nome do filme nos campos da tela
    def __str__(self):
        return f'{self.movie.title}'
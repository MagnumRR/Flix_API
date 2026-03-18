from django.db import models

# Create your models here.
# Classe Gênero

class Genre (models.Model):
    # O id é criado automaticamente!
    name = models.CharField(max_length=200)
    
    # Exibindo o nome dos objetos
    def __str__(self):
        return self.name
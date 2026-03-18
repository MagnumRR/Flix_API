from django.contrib import admin
# Importar ao app reviews o model Review
from reviews.models import Review

# Registrar no Admin do Djando a gestão do model Review
@admin.register(Review)
class AdminReview (admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')
    
    
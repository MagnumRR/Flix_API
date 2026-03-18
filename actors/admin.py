from django.contrib import admin
# Importando do projeto actors o model Actor
from actors.models import Actor
# Register your models here.

@admin.register(Actor)
class ActorAdmin (admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality')
# Register your models here.

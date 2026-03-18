# Importar do app atual (genres) todas as views
from . import views

# Importar do django - urls o módulo path
from django.urls import path

# Utilizar a variável urlpatterns para adicionar as urls
urlpatterns = [
    path('genres/', views.GenreCreateListView.as_view(), name='genre-list-view'),
    path('genres/<int:pk>/', views.GenreRetriveUpdateDestroyView.as_view(), name='genre-detail-view'),
]

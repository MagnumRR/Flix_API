# Importando do projeto movies o model Movie
from movies.models import Movie
# Importando do projeto movies o serializer correspondente
from movies.serializers import MovieModelSerializer
# Importando do rest_framework o módulo generics
from rest_framework import generics
# Importando a classe "Está autenticado" de Rest Framework
from rest_framework.permissions import IsAuthenticated
# Importando a classe global de permissões em app
from app.permissions import GlobalDefaultPermission

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer    
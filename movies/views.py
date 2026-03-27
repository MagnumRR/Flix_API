# Importando do projeto movies o model Movie
from movies.models import Movie
# Importando do projeto movies o serializer correspondente
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
# Importando do rest_framework o módulo generics
from rest_framework import generics, response, status
# Importando a classe "Está autenticado" de Rest Framework
from rest_framework.permissions import IsAuthenticated
# Importando a classe global de permissões em app
from app.permissions import GlobalDefaultPermission
# Importando do rest framework o módulo views
from rest_framework import views
# Importando A função "Count" de Django
from django.db.models import Count, Avg
# importando o model Review
from reviews.models import Review
# Importando a classe MovieStats de serializer
from .serializers import MovieStatsSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Movie.objects.all()
        
    # Utilizando o método get serializer para capturar o serializer adequado
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    
    # Utilizando o método get serializer para capturar o serializer adequado
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MovieListDetailSerializer
        return MovieModelSerializer

class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()

    def get(self, request):
        # Contando a quantidade de filmes
        total_movies = self.queryset.count()
        # Contando filmes por gênero
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        # Contando os reviews
        total_reviews = Review.objects.count()
        # Coletando a média de estrelas (stars)
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }
        serializer = MovieStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(data=serializer.data, status=status.HTTP_200_OK,)

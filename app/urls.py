from django.contrib import admin
from django.urls import path, include
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    return Response(
        {
            "message": "Bem vindo a API Filmes - Magnum",
            "version": "1.0",
            "endpoint": {
                "Gêneros": "api/v1/genres",
                "Atores": "api/v1/actors",
                "Filmes": "api/v1/movies",
                "Avaliações": "api/v1/reviews",
            }
        }
    )


urlpatterns = [
    path('', home, name='home'),  # o home foi direcionado para url do admin django
    path('admin/', admin.site.urls),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('authentication.urls')),
]

# Importar ao app reviews o model Review
from reviews.models import Review
# Importar do módulo rest_framework o módulo serializers
from rest_framework import serializers
# Importar do app movies o model Movie
from movies.models import Movie


# Serializer de Review
class ReviewSerializer(serializers.ModelSerializer):

    # Exibir o nome do filme, com base no id e permitir edição   
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all()
    )
    movie_title = serializers.CharField(source='movie.title', read_only=True)  # Exibir o título do filme, sem permitir edição

    class Meta:
        model = Review
        fields = ['id', 'movie','movie_title', 'stars', 'comment']

    def validate_stars(self, value):

        if 0 < value > 5:
            raise serializers.ValidationError('Somente notas entre 0 e 5.')
        return value

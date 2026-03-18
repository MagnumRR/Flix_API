# Importando do projeto movies o model Movie
from movies.models import Movie
# Importando do rest_framework o módulo serializers
from rest_framework import serializers
# Importando a função média (avg) do Django
from django.db.models import Avg

# Classe serializer do projeto movies
class MovieModelSerializer(serializers.ModelSerializer):
   
    genre = serializers.StringRelatedField()
    actors = serializers.StringRelatedField(many=True)
    # Media de avaliações
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'actors', 'resume', 'rate',]

    # Criando uma validação de data de lançamento
    def validate_release_date (self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1990.')
        return value
    
    # Para todo atributo do módulo "serializerMethodFiled" deverá ter um método relacionado
    def get_rate (self, obj):
        # recebe todas as reviews
        reviews = obj.reviews.all()
        
        # Utilizando a função "aggregate" para calcular a média de reviews
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
        if rate:
            return rate
        return "-"
                
    # Criando uma validação de limites de caracteres em comentários
    def validate_resume (self, value):
        if len(value) > 300:
            raise serializers.ValidationError('Somente 50 caracteres permitidos.')
        return value
    
'''# Classe serializer - construção manual (apenas para exemplo)
class MovieSerializer(serializers.Serializer): # do módulo serializers recebe a classe Serializer
    id = serializers.IntegerField() # Retorna o id do filme
    title = serializers.CharField() # retorna o Titulo do filme
    genre = serializers.StringRelatedField(
         # Retorna o genero do filme (nome)
    ) 
    release_date = serializers.DateField()
    actors = serializers.StringRelatedField( # exibe da tabela Actors somente o nome dos atores
        many=True
        
    )
    resume = serializers.CharField()
'''
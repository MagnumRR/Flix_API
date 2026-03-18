# Não será utilizada: from django.shortcuts import render
'''Importação de módulos sem utilização do DRF:
import json
from django.urls import path
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
'''

# Importação de módulos utilizando DRF:
from genres.models import Genre
from rest_framework import generics
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
from genres.permissions import GenrePermissionClass
from app.permissions import GlobalDefaultPermission

# Método de criação e listagem com DRF
class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all() # Recebe todos os itens da tabela "Genre"
    serializer_class = GenreSerializer # Designa o serializer

# Método de detalhamento, atualização e exclusão com DRF
class GenreRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genre.objects.all() # Recebe todos os itens da tabela "Genre"
    serializer_class = GenreSerializer # Designa o serializer


''' Método sem DRF
@csrf_exempt
def genre_create_list_view (request):
    # VERIFICAR TIPO DE REQUISIÇÃO
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse ({'id':new_genre.id, 'name':new_genre.name},status=201,)
'''

''' Método sem DRF
@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)    
    
    if request.method == "GET":
        data = ({'id':genre.id, 'name':genre.name})
        return JsonResponse(data)
    elif request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save() 
        return JsonResponse({'id':genre.id, 'name':genre.name})
    elif request.method == "DELETE":
        genre.delete()
        return JsonResponse({'message': 'Gênero excluído com sucesso!'},status=204)
'''    
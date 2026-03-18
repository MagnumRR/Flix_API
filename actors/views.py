# Importando do projeto "actors" a classe Model "Actor"
from actors.models import Actor
# Importando do módulo "rest_framework" o módulo "generics"
from rest_framework import generics
# Importando do projeto "actors" a classe "ActorSerializer"
from actors.serializer import ActorSerializer
# Importando do Rest_Framewor Permissões a classe de Autenticação
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
# Importando a classe global permissões de app
from app.permissions import GlobalDefaultPermission


class ActorCreateListView (generics.ListCreateAPIView):
    # aplica-se a classe de permissão a view correspondente
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveUpdateDesctroy (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission, )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
# Importando ao app reviews o model Review
from reviews.models import Review
# Importando ao app reviews o serializer de Review
from reviews.serializer import ReviewSerializer
# Importando do rest_framework o módulo generics
from rest_framework import generics
# Importando a classe "Está autenticado" de Rest Framework
from rest_framework.permissions import IsAuthenticated
# Importando a classe global de permissões em app
from app.permissions import GlobalDefaultPermission


# View para criação e listagem de Review:
class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# View para detalhar, atualizar e excluir uma Review:
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

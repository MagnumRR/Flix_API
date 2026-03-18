from . import views
from django.urls import path

urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actor-list-view'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDesctroy.as_view(), name='actor-detail-view'),
]

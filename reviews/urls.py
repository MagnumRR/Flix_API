from . import views
from django.urls import path


urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name='review-list-view'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]

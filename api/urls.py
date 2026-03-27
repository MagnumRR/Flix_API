from rest_framework.routers import DefaultRouter
from genres.views import GenreCreateListView, GenreRetriveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDesctroy
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


router = DefaultRouter()
router.register(r'genres', GenreCreateListView, GenreRetriveUpdateDestroyView)
router.register(r'actors', ActorCreateListView, ActorRetrieveUpdateDesctroy)
router.register(r'movies', MovieCreateListView, MovieRetrieveUpdateDestroyView)
router.register(r'reviews', ReviewCreateListView, ReviewRetrieveUpdateDestroyView)

urlpatterns = router.urls

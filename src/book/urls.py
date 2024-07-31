from django.urls import include, path
from rest_framework import routers

from src.book.views import AuthorView, BookView

router = routers.DefaultRouter()
router.register('books', BookView, "book")
router.register('author', AuthorView, "author")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

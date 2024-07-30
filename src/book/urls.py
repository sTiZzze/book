from rest_framework import routers
from django.urls import path, include

from src.book.views import BookView, AuthorView

router = routers.DefaultRouter()
router.register('books', BookView, "book")
router.register('author', AuthorView, "author")

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls

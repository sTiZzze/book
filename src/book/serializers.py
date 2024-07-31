from rest_framework.serializers import ModelSerializer

from src.book.models import Author, Book


class CreateBookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'author', 'language', 'pages', 'published_at', 'cover',)


class ReadBookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ('__all__')


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ('__all__')

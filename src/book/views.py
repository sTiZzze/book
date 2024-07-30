
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from src.book.serializers import CreateBookSerializer, AuthorSerializer, ReadBookSerializer
from src.book.models import Book, Author

from datetime import datetime


class BookView(ViewSet):

    def list(self, request):
        """List all books"""
        post = Book.objects.all()
        serializer = ReadBookSerializer(post, many=True)
        return Response({'data': serializer.data})

    def create(self, request, *args, **kwargs):
        form = CreateBookSerializer(data=request.data)
        form.is_valid(raise_exception=True)
        post = form.save(owner=request.user)
        return Response(status=status.HTTP_201_CREATED, data=CreateBookSerializer(post).data)

    def retrieve(self, request, pk):
        """Query any book"""
        posts = get_object_or_404(Book, pk=pk)
        self.check_object_permissions(request, posts)
        serializer = ReadBookSerializer(posts)
        return Response({'data': serializer.data})

    @action(detail=False, methods=['get'], url_path='books-in-range')
    def books_in_range(self, request):
        start_data = request.query_params.get('start_date')
        end_data = request.query_params.get('end_date')

        if not start_data or not end_data:
            return Response({"error": "Please provide both start_date and end_date"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_data = datetime.strptime(start_data, '%Y-%m-%d')
            end_data = datetime.strptime(end_data, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Date format should be YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)
        books = Book.objects.filter(created_date__range=[start_data, end_data]).order_by('-pages')
        print(books.query)
        serializer = ReadBookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

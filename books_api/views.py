from rest_framework import generics, viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

from books.models import Book, Category
from . import serializers


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('published_year',)


class BookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class FavoriteListAPIVew(generics.ListAPIView):
    serializer_class = serializers.BookSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return self.request.user.favorite_books.all()

from rest_framework import generics, viewsets
from django_filters import rest_framework as filters

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

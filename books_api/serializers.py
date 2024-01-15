from rest_framework import serializers

from books import models


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    slug = serializers.SlugField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"  # ("title", "description", ...)

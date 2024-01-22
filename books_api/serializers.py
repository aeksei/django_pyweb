from rest_framework import serializers

from books import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name", "slug")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"  # ("title", "description", ...)

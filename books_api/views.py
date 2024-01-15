from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import Book
from . import serializers


class BookAPIView(APIView):
    def get(self, request, pk: int):  # pk == id
        instance = Book.objects.get(pk=pk)  # pk=5

        serializer = serializers.BookSerializer(
            instance=instance  # принимает ORM объект
        )

        return Response(
            data=serializer.data  # python dict (json как текст)
            # data={
            #     "title": instance.title,
            #     ...
            # }
        )



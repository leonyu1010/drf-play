from rest_framework import viewsets

from server.apps.api.books.models import Book
from server.apps.api.books.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

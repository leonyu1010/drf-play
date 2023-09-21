from django.contrib import admin

from server.apps.api.books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin[Book]):
    """Admin panel example for ``Book`` model."""

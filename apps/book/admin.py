from django.contrib import admin
from apps.book.models import Book, Category

admin.site.register(Category)
admin.site.register(Book)

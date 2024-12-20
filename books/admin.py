from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'isbn','author', 'publish']
    list_filter=['publish', 'created']
    prepopulated_fields = {"slug":('title',)}
from django.contrib import admin
from books.models import Book, Review


# Register your models here.


class ReviewInLine(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ['title', 'author', 'price', ]


admin.site.register(Book, BookAdmin)

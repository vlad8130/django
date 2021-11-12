from django.contrib import admin

from .models import Article, Author, Comment, Like, Book

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Like)

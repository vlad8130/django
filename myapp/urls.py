from django.urls import path, re_path

from .views import index, first, articles, article_number, archive_num, phone_number, users, users_num, archive, \
    code

urlpatterns = [
    path('', index, name='index'),
    path('first', first, name='first'),
    path('articles/', articles, name='articles'),
    path('article/<int:article_id>/archive/', archive_num, name='archive_num'),
    path('articles/<int:article_id>/', article_number, name='article_number'),
    path('articles/<int:article_id>/<slug:name>/', article_number, name='article_name'),
    path('articles/archive/', archive, name='archive'),
    path('users/', users, name='users'),
    path('users/<int:user_number>/', users_num, name='users_num'),
    path('[0-9]{10}', phone_number, name='phone_number'),
    re_path('[0-9a-f]{4}[-][0-9a-f]{6}', code, name='code'),
]

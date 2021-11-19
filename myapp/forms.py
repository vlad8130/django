from django.forms import ModelForm
from .models import Author, Article


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['text', 'author']

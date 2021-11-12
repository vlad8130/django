import re

from django.http import HttpResponse
from django.shortcuts import render


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')

    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
    })


def first(request):
    name = 'Vladimir'
    return render(request, 'first.html', {
        'name': name,
    })


def articles(request):
    return render(request, 'articles.html')


def archive(request):
    return render(request, 'archive.html')


def users(request):
    return render(request, 'users.html')


def article_number(request, article_id, name=''):

    data = {'article_id': article_id, 'name': name}
    return render(request, 'article_number.html', {
        'check': article_id % 2,
        'slug': name
        })


def archive_num(request, article_id):
    return HttpResponse('{} archive Success!'.format(article_id))


def users_num(request, user_number):
    return HttpResponse('User {} Success!'.format(user_number))


def phone_number(request, phone_num):
    code_list = ['067', '068', '096', '097', '098', '050', '066', '095', '099', '063', '093', '091', '092', '094']
    if len(str(phone_num)) == 10:
        for i in code_list:
            result = re.match(i, str(phone_num))
            if result:
                return HttpResponse("Ukrainian phone number")
    return HttpResponse("Number is not valid")


def code(request):
    return HttpResponse('Your code is converted!')

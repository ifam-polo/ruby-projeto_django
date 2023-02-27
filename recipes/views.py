from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Ruby Carvalho',
        'idade': '23',
    })
from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(
        request, 
        'mal_userpage/index.html', 
        {'name': 'JJSakurai'}
        )
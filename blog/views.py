from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    print('blog')
    return HttpResponse('blog do APP 01')

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo do APP 01')
# from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    print('HOME')
    return HttpResponse('Home do APP 01')

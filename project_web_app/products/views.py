from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Welcome to python app!')

def new(request):
    return HttpResponse('New Products')
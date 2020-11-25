from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("hello world")

def man(request):
    return HttpResponse("man")

def findbook(request):
    return HttpResponse("Martin Iden")


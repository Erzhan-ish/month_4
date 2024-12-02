from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    if request.method == 'GET':
        return HttpResponse('Привет это мой первый проект на django')

def emoji(request):
    if request.method == 'GET':
        return HttpResponse('😆')

def image_proger_view(request):
    if request.method == 'GET':
        return HttpResponse('<img ')



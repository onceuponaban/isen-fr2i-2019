from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'quiz/home.html', locals())

def play(request):
    return render(request, 'quiz/play.html', locals())

def ranking(request):
    return render(request, 'quiz/ranking.html', locals())

def signin(request):
    return render(request, 'quiz/signin.html', locals())

def modif(request):
    return render(request, 'quiz/modif.html', locals())    


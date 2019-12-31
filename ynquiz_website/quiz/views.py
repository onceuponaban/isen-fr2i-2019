from django.http import HttpResponse
from django.shortcuts import render
from quiz.models import Answer
from quiz.models import Question

def home(request):
    return render(request, 'quiz/home.html', locals())

def play(request):
    answers = Answer.objects.filter(question__id=1)
    question = Question.objects.filter(id=1)
    return render(request, 'quiz/play.html', {'reponses': answers, 'question': question[0]})

def ranking(request):
    return render(request, 'quiz/ranking.html', locals())

def signin(request):
    return render(request, 'quiz/signin.html', locals())
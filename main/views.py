from django.shortcuts import render, redirect
from news.models import *
from main.models import *


# Create your views here.
def index(request):
    news = News.objects.filter().order_by('-date')[:3]
    informations = Information.objects.all()
    return render(request, 'static/main/index.html', {'news': news, 'informations': informations})


def frequent_questions(request):
    questions = FrequentQuestions.objects.all()
    return render(request, 'static/main/frequent_questions.html', {'questions': questions})


def redirect_from_root(request):
    return redirect(to='/main/')

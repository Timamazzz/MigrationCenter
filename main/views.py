from django.shortcuts import render, redirect
from news.models import *
from main.models import *


# Create your views here.
def index(request):
    posts = Post.objects.filter().order_by('-date')[:3]
    banner_posts = Post.objects.exclude(bannerImage='').order_by('-date')[:3]
    informations = Information.objects.filter().order_by('-date')[:4]
    return render(request, 'main/index.html',
                  {'posts': posts, 'informations': informations, 'banners': banner_posts})


def frequent_questions(request):
    questions = FrequentQuestions.objects.all()
    return render(request, 'main/frequent_questions.html', {'questions': questions})


def redirect_from_root(request):
    return redirect(to='/main/')


def handler404(request, exception):
    return render(request, '404.html', status=404)


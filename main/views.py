from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from news.models import *
from main.models import *


# Create your views here.
def index(request):
    title = 'Миграционный центр'
    posts = Post.objects.filter().order_by('-date')[:3]
    banner_posts = Post.objects.exclude(bannerImage='').order_by('-date')[:3]
    informations = Information.objects.filter().order_by('-date')[:4]

    if request.method == 'POST':
        info = Information.objects.get(id=int(request.POST.get('id')))
        name = info.header
        text = info.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'main/index.html',
                      {'posts': posts, 'informations': informations, 'banners': banner_posts, 'title': title})


def frequent_questions(request):
    title = 'Частые вопросы'
    questions = FrequentQuestions.objects.all()
    return render(request, 'main/frequent_questions.html', {'questions': questions, 'title': title})


def redirect_from_root(request):
    return redirect(to='/main/')


def handler404(request, exception):
    title = 'Не найдено'
    return render(request, '404.html', {'title': title}, status=404)

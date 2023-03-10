from django.http import JsonResponse
from django.shortcuts import render, redirect
from news.models import *
from main.models import *


# Create your views here.
def index(request):
    title = 'Центр помощи, поддержки, социальной и трудовой адаптации'
    posts = Post.objects.filter().order_by('-date')[:3]
    banners = MainBanner.objects.filter(is_active=True).order_by('-date')
    informations = Information.objects.filter().order_by('-date')[:4]

    if request.method == 'POST':
        info = Information.objects.get(id=int(request.POST.get('id')))
        name = info.header
        text = info.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'main/index.html',
                      {'posts': posts, 'informations': informations, 'banners': banners, 'title': title})


def frequent_questions(request):
    title = 'Частые вопросы'
    questions = FrequentQuestions.objects.all()
    return render(request, 'main/frequent_questions.html', {'questions': questions, 'title': title})


def redirect_from_root(request):
    return redirect(to='/main/')


def informations(request):
    title = 'Информация'
    informations = Information.objects.all()
    if request.method == 'POST':
        info = Information.objects.get(id=int(request.POST.get('id')))
        name = info.header
        text = info.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'main/informations.html', {'informations': informations, 'title': title})

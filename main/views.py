from django.shortcuts import render, redirect
from news.models import *
from main.models import *


# Create your views here.
def index(request):
    news = News.objects.all()
    informations = Information.objects.all()
    return render(request, 'dist/index.html', {'news': news, 'informations':informations})


def redirect_from_root(request):
    return redirect(to='/main/')

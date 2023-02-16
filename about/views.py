from django.shortcuts import render
from .models import *


# Create your views here.
def us(request):
    return render(request, 'static/about/us.html')


def area_of_activities(request):
    return render(request, 'static/about/area_of_activities.html')


def docs(request):
    return render(request, 'static/about/docs.html')


def vacancies(request):
    return render(request, 'static/about/vacancies.html')

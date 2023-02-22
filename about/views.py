from django.shortcuts import render
from .models import *


# Create your views here.
def us(request):
    docs = Document.objects.filter(type='Additional_activity')
    return render(request, 'static/about/us.html', {'docs': docs})


def area_of_activities(request):
    docs = Document.objects.filter(type='AreaOfActivity')
    return render(request, 'static/about/area_of_activities.html', {'docs': docs})


def docs(request):
    regular_docs = Document.objects.filter(type='Regulation')
    other_docs = Document.objects.filter(type='Other')

    return render(request, 'static/about/docs.html', {'regular': regular_docs, 'other': other_docs})


def vacancies(request):
    vacancies = Vacancy.objects.filter(is_active=True)
    return render(request, 'static/about/vacancies.html', {'vacancies': vacancies})

from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def us(request):
    docs = Document.objects.filter(type='Additional_activity')

    if request.method == 'POST':
        doc = Document.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        text = doc.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'about/us.html', {'docs': docs})


def area_of_activities(request):
    docs = Document.objects.filter(type='AreaOfActivity')

    if request.method == 'POST':
        doc = Document.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        text = doc.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'about/area_of_activities.html', {'docs': docs})


def docs(request):
    regular_docs = Document.objects.filter(type='Regulation')
    other_docs = Document.objects.filter(type='Other')

    if request.method == 'POST':
        doc = Document.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        text = doc.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'about/docs.html', {'regular': regular_docs, 'other': other_docs})


def vacancies(request):
    vacancies = Vacancy.objects.filter(is_active=True)
    return render(request, 'about/vacancies.html', {'vacancies': vacancies})

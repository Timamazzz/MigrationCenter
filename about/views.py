from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import *
from django.template.loader import render_to_string


# Create your views here.
def us(request):
    docs = AdditionalActivity.objects.all()
    title = 'О нас'

    if request.method == 'POST':
        doc = AdditionalActivity.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        text = doc.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'about/us.html', {'docs': docs, 'title': title})


def area_of_activities(request):
    docs = AreaOfActivity.objects.all()
    title = 'Направления деятельности'

    if request.method == 'POST':
        doc = AreaOfActivity.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        text = doc.text
        return JsonResponse({'name': name, 'text': text})
    else:
        return render(request, 'about/area_of_activities.html', {'docs': docs, 'title': title})


def docs(request):
    regular_docs = Document.objects.filter(type='Regulation')
    other_docs = Document.objects.filter(type='Other')
    report_docs = Document.objects.filter(type='Reporting')
    title = 'Документы'

    if request.method == 'POST':
        doc = Document.objects.get(id=int(request.POST.get('id')))
        name = doc.name
        images = DocImage.objects.filter(document__id=doc.id)
        images = serializers.serialize('json', images)
        return JsonResponse({'name': name, 'images': images})
    else:
        return render(request, 'about/docs.html', {'regular': regular_docs, 'other': other_docs,
                                                   'reports': report_docs, 'title': title})


def vacancies(request):
    title = 'Вакансии'
    vacancies = Vacancy.objects.filter(is_active=True)
    return render(request, 'about/vacancies.html', {'vacancies': vacancies, 'title': title})

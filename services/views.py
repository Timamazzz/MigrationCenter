from django.shortcuts import render
from .models import *

# Create your views here.
def services(request):
    title = 'Услуги'
    return render(request, 'services/services.html', {'title': title})


def insurance(request):
    title = 'Страхование'
    services = InsuranceService.objects.all()
    return render(request, 'services/insurance.html', {'title': title, 'services': services})


def testing(request):
    title = 'Тестирование'
    return render(request, 'services/testing.html', {'title': title})


def translation(request):
    title = 'Перевод'
    return render(request, 'services/translation.html', {'title': title})
from django.shortcuts import render


# Create your views here.
def services(request):
    title = 'Услуги'
    return render(request, 'services/services.html', {'title': title})


def insurance(request):
    title = 'Страхование'
    return render(request, 'services/insurance.html', {'title': title})


def testing(request):
    title = 'Тестирование'
    return render(request, 'services/testing.html', {'title': title})


def translation(request):
    title = 'Перевод'
    return render(request, 'services/translation.html', {'title': title})
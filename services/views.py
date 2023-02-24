from django.shortcuts import render


# Create your views here.
def services(request):
    return render(request, 'services/services.html')


def insurance(request):
    return render(request, 'services/insurance.html')


def testing(request):
    return render(request, 'services/testing.html')


def translation(request):
    return render(request, 'services/translation.html')
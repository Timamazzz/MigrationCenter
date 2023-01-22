from django.shortcuts import render
from .models import *


# Create your views here.
def history(request):
    histories = History.objects.all()
    return render(request, 'dist/history.html', {'histories': histories})

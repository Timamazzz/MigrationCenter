from django.shortcuts import render
from contacts.models import *


# Create your views here.
def contacts(request):
    contacts = Contact.objects.all()
    managers = Manager.objects.all()
    title = 'Контакты'

    return render(request, 'contacts/contacts.html', {'contacts': contacts, 'managers': managers, 'title': title})

from django.shortcuts import render


# Create your views here.
def feedback(request):
    title = 'Контакты'
    return render(request, 'feedback/feedback.html', {'title': title})

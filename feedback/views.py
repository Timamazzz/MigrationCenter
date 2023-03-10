from django.shortcuts import render


# Create your views here.
def feedback(request):
    title = 'Обратная связь'
    return render(request, 'feedback/feedback.html', {'title': title})

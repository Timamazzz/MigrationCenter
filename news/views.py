from django.shortcuts import render


# Create your views here.
def news(request):
    return render(request, 'static/news/news.html')


def post(request):
    return render(request, 'static/news/post.html')
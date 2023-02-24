from django.shortcuts import render
from news.models import *


# Create your views here.
def news(request):
    posts = Post.objects.all()
    return render(request, 'news/news.html', {'posts': posts})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    gallery = PostImage.objects.filter(news__id=post_id)
    return render(request, 'news/post.html', {'post': post, 'gallery': gallery})

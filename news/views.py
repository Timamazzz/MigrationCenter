from django.shortcuts import render
from news.models import *


# Create your views here.
def news(request):
    title = 'Новости'
    posts = Post.objects.all()
    return render(request, 'news/news.html', {'posts': posts, 'title': title})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    gallery = PostImage.objects.filter(news__id=post_id)
    title = post.header
    return render(request, 'news/post.html', {'post': post, 'gallery': gallery, 'title': title})

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('post/', views.post, name='post'),
]

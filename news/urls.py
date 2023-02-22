from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('post/<int:post_id>', views.post, name='post'),
]

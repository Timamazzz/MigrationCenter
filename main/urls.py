from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('questions/', views.frequent_questions, name='questions'),
]

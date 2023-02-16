from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('insurance/', views.insurance, name='insurance'),
    path('testing/', views.testing, name='testing'),
    path('translation/', views.translation, name='translation'),
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.us, name='us'),
    path('areaOfActivities/', views.area_of_activities, name='area_of_activities'),
    path('docs/', views.docs, name='docs'),
    path('vacancies/', views.vacancies, name='vacancies'),
]

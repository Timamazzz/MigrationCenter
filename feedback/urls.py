from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.FeedbackCreateView.as_view(), name='feedback')
]

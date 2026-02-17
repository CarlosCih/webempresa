from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesPageView.as_view(), name='services'),
]
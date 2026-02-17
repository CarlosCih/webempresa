from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('services/', views.ServicesPageView.as_view(), name='services'),
    path('blog/', views.BlogPageView.as_view(), name='blog'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('store/', views.StorePageView.as_view(), name='store'),
    path('samples/', views.SamplesPageView.as_view(), name='samples'),
]

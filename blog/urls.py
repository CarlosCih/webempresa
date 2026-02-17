from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog'),
    path('category/<int:category_id>/', views.BlogPageView.category, name='blog_category'),
]
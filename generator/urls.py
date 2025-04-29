# generator/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/generate/', views.generate_image_view, name='generate_image'),
]

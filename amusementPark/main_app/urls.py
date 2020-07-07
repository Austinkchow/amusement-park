from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.admin, name='admin'),
]

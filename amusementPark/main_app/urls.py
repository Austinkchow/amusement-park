from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.admin, name='admin'),
    path('signup/', views.signup, name='signup'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('subscribed/', views.subscribed, name='subscribed'),
]

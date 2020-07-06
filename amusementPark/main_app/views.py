from django.shortcuts import render
from django.http import HttpResponse


# Home Page
def home(request):
  return render(request, 'home.html')


def admin(request):
    return render(request, 'admin.html')
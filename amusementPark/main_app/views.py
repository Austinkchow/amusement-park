from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Home Page
def home(request):
  return render(request, 'home.html')


def admin(request):
    user = User.objects.all()
    context = {
      'user': user
    }
    return render(request, 'admin.html', context)


#  TODO
#  need to validate (min length, ".", "@")
#  make a min length validator


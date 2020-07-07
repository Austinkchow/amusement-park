from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import Sign_Up_Form

# Home Page
def home(request):
  return render(request, 'home.html')


def admin(request):
    users = User.objects.all()
    context = {
      'users': users
    }
    return render(request, 'admin.html', context)

def signup(request):
  error_message=''
  if request.method == 'POST':
    form = Sign_Up_Form(request.POST)
    if form.is_valid():
      if len(request.POST['firstName'])<2:
        error_message= 'First name must contain at least two characters'
      elif len(request.POST['lastName'])<2:
        error_message= 'Last name must contain at least two characters'
      else:
        form.save()
        return redirect('subscribed')
  else:
    form = Sign_Up_Form()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request,'signup.html', context)

def subscribed(request):
  return render(request, 'subscribed.html')

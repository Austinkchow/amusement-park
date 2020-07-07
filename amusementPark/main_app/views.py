from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Home Page
def home(request):
  return render(request, 'home.html')

# Admin Page
# TODO 
# Should list user firstName, lastName, email, and preferences
# solved bug for user info not displaying on admin.html page by changing 'user' to 'users' 
def admin(request):
    users = User.objects.all()   
    context = {
      'users': users,
    }
    print(users)
    return render(request, 'admin.html', context)


#  TODO
#  need to validate (min length, ".", "@")



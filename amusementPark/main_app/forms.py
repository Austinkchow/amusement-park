from django.forms import ModelForm
from django import forms
from .models import User

class Sign_Up_Form(ModelForm):
    class Meta:
        model = User
        fields = ['firstName','lastName','email' ]
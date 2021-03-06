from dataclasses import field
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class techolasUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','password1','password2']
        labels={
            'first_name':'Name',
            'email':'Email',
        }
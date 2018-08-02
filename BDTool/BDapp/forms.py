from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import AuthenticationForm, UsernameField
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from .models import Project, Client ,Technology

class Project_Form(forms.ModelForm):

    class Meta:
        model=Project
        fields=['project_name','technology','url_name','domain_name','project_desrciption']

class Client_Form(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class User(AbstractUser):
    class Meta(object):
        unique_together = ('email',)


class EmailBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}), label=("Email"))

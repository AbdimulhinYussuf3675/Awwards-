from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Projects

class UpdateUser(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','email']

class UpdateProfile(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['profile_pic','bio']

class ProjectsForm(forms.ModelForm):

    class Meta:
      model = Projects

      fields = ['title', 'image', 'project_description', 'user', 'site', 'country']    
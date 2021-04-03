from app.models import User
from django import forms
from django.forms import ModelForm

class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
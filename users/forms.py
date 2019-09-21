from django.contrib.auth.models import AbstractUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = AbstractUser
		fields = ('username','email')

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = AbstractUser
		fields = ('username', 'email')

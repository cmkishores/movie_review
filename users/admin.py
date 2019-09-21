from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = AbstractUser


admin.site.register(AbstractUser, CustomUserAdmin)

# Register your models here.

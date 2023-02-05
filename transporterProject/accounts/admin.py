from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.

UserModel = get_user_model()

@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    pass
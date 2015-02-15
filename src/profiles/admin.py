from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from authtools.admin import NamedUserAdmin
from .models import Profile
from django.conf import settings
from django.contrib.auth import get_user_model
#from authtools import User as NewUser

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(NamedUserAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

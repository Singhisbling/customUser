from django.contrib import admin
from .models import *
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
#from django import forms


class custom(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',)
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )






admin.site.register(customUser,custom)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Technology)
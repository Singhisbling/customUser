from django.contrib import admin
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django import forms

class UserCreationFormExtended(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationFormExtended, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label=_("E-mail"), max_length=75,required = True)

    def clean(self):
        email = self.cleaned_data.get("email")
        email_list = self.cleaned_data.get("email")
        if email in email_list:
            raise forms.ValidationError(
                self.error_messages['email already exist'],
            )
        return email

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ( 'username','email', 'password1', 'password2',)
    }),
)


admin.site.register(customUser)
admin.site.register(Project)
admin.site.register(Client)
admin.site.register(Technology)
#admin.site.register()
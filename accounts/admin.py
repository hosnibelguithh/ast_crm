from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeCreationForm, CustomUserCreationForm
from .models import CustomUser

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('phonenumber','Agent','Admin')}),
)
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeCreationForm
    list_filter = ("Admin","Agent" )
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS

admin.register(CustomUserAdmin)
    





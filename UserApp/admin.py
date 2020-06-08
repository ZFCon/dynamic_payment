from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as UserAdminAbstract
from django.utils.translation import gettext, gettext_lazy as _
from .models import *
from Payment.models import Transaction


class TransactionInline(admin.TabularInline):
    model = Transaction
    extra = 0
    


@admin.register(User)
class UserAdmin(UserAdminAbstract):
    list_display = ['username', 'first_name', 'last_name', 'balance', 'is_staff']
    inlines = [TransactionInline]

    fieldsets = fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Payment'), {'fields': ('balance',)}),
    )
    readonly_fields = ['balance']

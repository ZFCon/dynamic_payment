from django.contrib import admin
from django import forms
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.admin import UserAdmin

from .models import *

class PromoForm(forms.ModelForm):
    class Meta:
        widgets = {
          'discount_type': forms.RadioSelect
        }

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ['code', 'discount']
    form = PromoForm
    fieldsets = [
        (None, {'fields': ('code', )}),
        (_('Discount'), {'fields': ('discount', 'discount_type')}),
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'promo', 'status', 'created']
    readonly_fields = ['price']

@admin.register(PlaceHolder)
class PlaceHolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'paid']


class TransactionForm(forms.ModelForm):
    class Meta:
        widgets = {
          'transaction_type': forms.RadioSelect
        }

@admin.register(Transaction)
class Transaction(admin.ModelAdmin):
    list_display = ['user', 'order', 'created']
    form = TransactionForm
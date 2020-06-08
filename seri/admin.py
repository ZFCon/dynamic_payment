from django.contrib import admin

from .models import *



@admin.register(GG)
class GGAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass
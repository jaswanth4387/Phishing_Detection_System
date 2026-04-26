from django.contrib import admin
from .models import AdminControl


@admin.register(AdminControl)
class AdminControlAdmin(admin.ModelAdmin):
    list_display = []
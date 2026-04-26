from django.contrib import admin
from .models import Prediction


@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'result', 'created_at')
    search_fields = ('url', 'user__username')
    list_filter = ('result', 'created_at')
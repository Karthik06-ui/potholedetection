from django.contrib import admin
from .models import PotholeEvent


@admin.register(PotholeEvent)
class PotholeEventAdmin(admin.ModelAdmin):
    list_display = ['id', 'severity', 'latitude', 'longitude', 'vibration_value', 'created_at']
    list_filter = ['severity', 'created_at']
    ordering = ['-created_at']
    readonly_fields = ['severity', 'created_at']
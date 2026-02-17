from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at', 'updated_at')
    search_fields = ('title', 'subtitle', 'content')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    
admin.site.register(Service, ServiceAdmin)

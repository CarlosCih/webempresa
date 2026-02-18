from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')
    ordering = ('name',)

admin.site.register(Link, LinkAdmin)

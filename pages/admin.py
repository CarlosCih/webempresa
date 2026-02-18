from django.contrib import admin

from pages.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
    list_filter = ('created', 'updated')
admin.site.register(Page, PageAdmin)

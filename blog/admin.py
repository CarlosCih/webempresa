from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'published', 'post_categories', 'created_at')
    search_fields = ('title', 'content', 'author__username', 'category__name',)
    date_hierarchy = 'published'
    ordering = ('author', 'published')
    
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.category.all().order_by("name")])
    post_categories.short_description = 'Categorías'
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

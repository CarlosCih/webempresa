from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from core.views import get_context_global

# Create your views here.
class BlogPageView(TemplateView):
    template_name = 'blog/blog.html'
    
    def category(request, category_id):
        category = get_object_or_404(Category, id=category_id)
        context = {
            'current_section': 'blog',
            'blogs': Post.objects.filter(category=category),
            'category': category,
        }
        context.update(get_context_global(request))
        return render(request, 'blog/blog_category.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'blog'
        context['blogs'] = Post.objects.all()
        context.update(get_context_global(self.request))
        return context
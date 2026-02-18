from django.views.generic import TemplateView
from core.navbar_ctx import get_context_global

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'home'
        context['message'] = 'Bienvenido a nuestra empresa'
        context.update(get_context_global(self.request))
        return context  


class ContactPageView(TemplateView):
    template_name = 'core/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'contact'
        context.update(get_context_global(self.request))    
        return context

class AboutPageView(TemplateView):
    template_name = 'core/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'about'
        context.update(get_context_global(self.request))
        return context

class StorePageView(TemplateView):
    template_name = 'core/store.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'store'
        context.update(get_context_global(self.request))
        return context

class SamplesPageView(TemplateView):
    template_name = 'core/sample.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'samples'
        context.update(get_context_global(self.request))
        return context


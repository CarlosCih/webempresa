from django.shortcuts import render
from django.views.generic import TemplateView
from core.views import get_context_global
from .models import *

# Create your views here.
class ServicesPageView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'services'
        context['services'] = Service.objects.all()
        context.update(get_context_global(self.request))
        return context
    
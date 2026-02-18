from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from core.navbar_ctx import get_context_global
from django.views.generic import TemplateView
from .forms import ContactForm

# Create your views here.
class ContactPageView(TemplateView):
    template_name = 'contact/contact.html'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = ContactForm()
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = self.get_context_data(**kwargs)
        
        if form.is_valid():
            # Obtener datos del formulario
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            # Enviar correo electrónico
            try:
                send_mail(
                    subject=f'Mensaje de contacto de {name}',
                    message=f'De: {name}\nCorreo: {email}\n\nMensaje:\n{content}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                context['form'] = ContactForm()  # Formulario vacío
                context['success'] = True
            except Exception as e:
                context['form'] = form
                context['error'] = 'Hubo un error al enviar el mensaje. Por favor, intenta de nuevo.'
        else:
            context['form'] = form
        
        return self.render_to_response(context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_section'] = 'contact'
        context.update(get_context_global(self.request))
        return context
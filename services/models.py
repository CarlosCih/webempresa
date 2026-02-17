from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, blank=True, verbose_name='Subtítulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name='Imagen')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado el')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created_at']
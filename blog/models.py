from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la categoría', unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título del post')
    content = models.TextField(verbose_name='Contenido del post')
    published = models.DateTimeField(default=now, verbose_name='Fecha de publicación')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name='Imagen del post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    category = models.ManyToManyField(Category, verbose_name='Categorías')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
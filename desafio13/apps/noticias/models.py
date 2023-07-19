from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nombre
    
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    autor = models.CharField(max_length=20, null=False)
    descripcion = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    imagen = models.ImageField(null=True, blank=True, upload_to='noticias', default='static/img/notidefault.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('-published',)    
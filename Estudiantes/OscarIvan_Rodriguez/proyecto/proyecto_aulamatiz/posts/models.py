from django.db import models

# Create your models here.

class Post(models.Model):
    
    #title es el nombre de la columna y permite un maximo de 100 caracteres
    titulo = models.CharField(max_length=100, help_text="Titulo del post")
    #la columna content es un campo de texto que puede contener una cantidad ilimitada de caracteres
    contenido = models.TextField()
    #la fecha de creacion
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # puntuacion del post
    puntuacion = models.FloatField(default=0)
    # activo
    activo = models.BooleanField(default=True)
    #Se puede crear indices para mejorar el rendimiento de las consultas
    class Meta:
        indexes = [
            models.Index(fields=['titulo']),
            models.Index(fields=['fecha_creacion']),
            
        ]

    ##ruta de migracion para crear elimnar o modificar la tabla en la base de datos
    ## python manage.py migrate
    ## python manage.py makemigrations
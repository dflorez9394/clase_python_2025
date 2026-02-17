from django.db import models
#ORM
#Object Relation Map
# Create your models here.

class Post(models.Model):
    """
    Model POST
    un model Represenra una tabla en la base de datos y cada instancia de post ocorresponde a un registr
    """
    #title es el nombre la columna,  y permite un maximo de 100 caracteres
    title = models.CharField(max_length=100)
    #la columna content permite "infinitos"  caracteres
    content = models.TextField()
    #la fecha de creacion
    created_at = models.DateTimeField(auto_now_add=True)

    rating = models.FloatField(default=0)
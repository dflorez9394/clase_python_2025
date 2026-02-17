from django.contrib import admin
from posts.models import Post ##traer el modelo post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_details_fields = ['titulo', 'fecha_creacion', 'puntuacion', 'activo'] ##campos que se muestran en la lista de posts
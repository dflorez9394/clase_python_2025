from django.contrib import admin

#nos traemos el modelo de post
from posts.models import Post

#vamos a añadir un decorador para registrar la clse en el panel admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #parametros del modelo quiero que se veam
    list_details_fields = ['title','created_at']
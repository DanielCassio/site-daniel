from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuração da exibição dos Posts na interface de administração do Django.
    """
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('author', 'created_at')
    # Preenche o campo 'slug' automaticamente com base no 'title' ao criar um post.
    prepopulated_fields = {'slug': ('title',)}

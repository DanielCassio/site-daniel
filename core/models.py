from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    """
    Representa um post do blog no banco de dados.
    """
    title = models.CharField(max_length=200, verbose_name="Título")
    # Adicionamos o campo de imagem. As imagens serão salvas na pasta 'media/post_images/'
    # blank=True e null=True tornam o campo opcional.
    post_image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name="Imagem do Post")
    content = models.TextField(verbose_name="Conteúdo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    slug = models.SlugField(max_length=255, unique=True, blank=True, help_text="Deixe em branco para gerar automaticamente a partir do título.")

    def __str__(self):
        """
        Retorna a representação em string do objeto, que é o título do post.
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para gerar o slug automaticamente
        a partir do título se ele não for fornecido.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        # Ordena os posts pela data de criação, do mais novo para o mais antigo.
        ordering = ['-created_at']

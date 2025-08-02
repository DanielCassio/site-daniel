from django.contrib import admin
from django.urls import path, include
# Importações necessárias
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota para a interface de administração do Django.
    path('admin/', admin.site.urls),
    # Inclui as URLs do aplicativo 'core' na raiz do site.
    path('', include('core.urls', namespace='core')),
]

# Adiciona a rota para servir arquivos de mídia em modo de desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

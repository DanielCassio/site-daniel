from django.urls import path
from . import views

# Define um namespace para as URLs deste app, para evitar conflitos.
app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),
]

from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    """
    View para a página inicial (Portfólio).
    Busca os 3 posts mais recentes para exibi-los como projetos em destaque.
    """
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'core/home.html', context)

def post_list(request):
    """
    View para a página do blog, que lista todos os posts.
    """
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'core/post_list.html', context)

def post_detail(request, slug):
    """
    View para exibir os detalhes de um único post do blog.
    """
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'core/post_detail.html', context)

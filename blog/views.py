from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts,
    }

    return render(request, 'index.html', context)

def postagem(request, id):
    post = Post.objects.get(pk=id)
    context = {
        "post": post,
    }
    return render(request, 'post.html', context)

def referencia(request):
    referencia = Post.objects.all()

    context = {
        "referencia" : referencia,
    }

    return render(request, 'referencias.html', context)

def aluno(request):
    aluno = Post.objects.all()

    context = {
        "aluno" : aluno,
    }

    return render(request, 'alunos.html', context)
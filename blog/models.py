from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=600)
    conteudo = models.TextField(max_length=1200)
    imagem = models.ImageField(blank=True)
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
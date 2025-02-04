from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>', views.postagem, name='postagem'),
    path('referencia/', views.referencia, name='referencia'),
    path('aluno/', views.aluno, name='aluno')
]
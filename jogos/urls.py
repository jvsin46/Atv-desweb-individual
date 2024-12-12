from django.urls import path
from .views import (
    CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView,
    JogoListView, JogoCreateView, JogoUpdateView, JogoDeleteView
)

urlpatterns = [
    # URLs para Categoria
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/novo/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria-update'),
    path('categorias/<int:pk>/excluir/', CategoriaDeleteView.as_view(), name='categoria-delete'),

    # URLs para Jogo
    path('jogos/', JogoListView.as_view(), name='jogo-list'),
    path('jogos/novo/', JogoCreateView.as_view(), name='jogo-create'),
    path('jogos/<int:pk>/editar/', JogoUpdateView.as_view(), name='jogo-update'),
    path('jogos/<int:pk>/excluir/', JogoDeleteView.as_view(), name='jogo-delete'),
]

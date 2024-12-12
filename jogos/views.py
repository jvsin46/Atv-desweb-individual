from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Jogo, Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'jogos/categoria_list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    fields = ['nome']
    success_url = reverse_lazy('categoria-list')
    template_name = 'jogos/categoria_form.html'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ['nome']
    success_url = reverse_lazy('categoria-list')
    template_name = 'jogos/categoria_form.html'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    success_url = reverse_lazy('categoria-list')
    template_name = 'jogos/categoria_confirm_delete.html'

class JogoListView(ListView):
    model = Jogo
    template_name = 'jogos/jogo_list.html'

class JogoCreateView(CreateView):
    model = Jogo
    fields = ['nome', 'descricao', 'categoria']
    success_url = reverse_lazy('jogo-list')
    template_name = 'jogos/jogo_form.html'

class JogoUpdateView(UpdateView):
    model = Jogo
    fields = ['nome', 'descricao', 'categoria']
    success_url = reverse_lazy('jogo-list')
    template_name = 'jogos/jogo_form.html'

class JogoDeleteView(DeleteView):
    model = Jogo
    success_url = reverse_lazy('jogo-list')
    template_name = 'jogos/jogo_confirm_delete.html'

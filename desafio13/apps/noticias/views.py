from django.shortcuts import render
from typing import Any, Dict
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Noticia, Categoria

# Create your views here.
def list(request):
    template_name = 'noticias/list.html'
    return render(request,template_name)

class ListNotice(ListView):
    model = Noticia
    template_name = 'noticias/list.html'
    context_object_name = "noticias"

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context['categorias'] = categorias
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')


class AddNotice(CreateView):
    model = Noticia
    fields = ['titulo', 'autor', 'descripcion', 'published', 'imagen', 'categoria']
    template_name = 'noticias/new_notice.html'
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        #form.instance.colaborador = self.request.user
        return super().form_valid(form)

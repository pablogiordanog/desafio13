from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .models import Noticia

# Create your views here.
def list(request):
    template_name = 'noticias/list.html'
    return render(request,template_name)


class AddNotice(CreateView):
    model = Noticia
    fields = ['titulo', 'autor', 'descripcion', 'published', 'imagen', 'categoria']
    template_name = 'noticias/new_notice.html'
    success_url = reverse_lazy('list')
    
    def form_valid(self, form):
        #form.instance.colaborador = self.request.user
        return super().form_valid(form)

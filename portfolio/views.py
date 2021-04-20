from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Portafolio, Categoria
from .forms import CreateProduct

# Create your views here.
class PortfolioView (ListView):
    model = Portafolio
    template_name = "portfolio-index.html"
    paginate_by = 4
    ordering = '-fecha'

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['categories'] = Categoria.objects.order_by('titulo').all()
        data['categories'] = data['categories']
        data['tittle'] = 'Portafolio - Anconi'
        data['link'] = self.request.path

        return data

class PortfolioCreate(CreateView):
    model = Portafolio
    template_name = 'portfolio-create.html'
    form_class = CreateProduct

class PortfolioUpdate(UpdateView):
    model = Portafolio
    template_name = 'portfolio-create.html'
    form_class = CreateProduct


class PortfolioDetail(DetailView):
    model = Portafolio
    template_name = 'portfolio-detail.html'

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['related'] = Portafolio.objects.order_by('-fecha').filter(categoria__titulo = self.object.categoria.titulo).exclude(pk = self.object.pk)
        data['related'] = data['related'][:4]
        data['tittle'] =  self.object.titulo +  '- Portafolio Anconi'
        return data
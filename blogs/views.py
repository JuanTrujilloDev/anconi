from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Blog, Categoria
from .forms import BlogCreateForm, SearchForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

class BlogHome (ListView):
    model = Blog
    template_name = "blog-index.html"
    ordering = ['-fecha']
    paginate_by = 12
  

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:3]
        data['categorias'] = Categoria.objects.all()
        data['search'] = SearchForm
        data['tittle'] = 'Blog - Anconi'

        return data

   


class BlogDetail(DetailView):
    model = Blog
    template_name = "blog-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:3]
        data['categorias'] = Categoria.objects.all()
        data['search'] = SearchForm
        obj = data['object']
        data['link'] = reverse_lazy('blog-detail', args = (self.object.slug, )) 
        data['tittle'] = self.object.titulo + ' - Blog Anconi'
        try:
            data["next_obj"] = Blog.get_next_by_fecha(obj)
        except:
            data["next_obj"] = False

        try:
            data["prev_obj"] = Blog.get_previous_by_fecha(obj)
        except:
            data["prev_obj"] = False

        return data



class BlogCreate(LoginRequiredMixin, CreateView):
    template_name = "blog-create.html"
    model = Blog
    form_class = BlogCreateForm

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['tittle'] = 'Nuevo Post - Anconi'

        return data

    def get_success_url(self):
        return reverse_lazy('blog-detail', args = (self.object.slug, ))

    def form_valid(self, form):
        obj= form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

class BlogEdit(LoginRequiredMixin, UpdateView):
    template_name = "blog-create.html"
    model = Blog
    form_class = BlogCreateForm

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['tittle'] = self.object.titulo + '- Edicion Blog'

        return data

    def get_success_url(self):
        return reverse_lazy('blog-detail', args = (self.object.slug, ))

    def form_valid(self, form):
        obj= form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)
    

class BlogDelete(LoginRequiredMixin, DeleteView):
    template_name = "blog-delete.html"
    model = Blog

    def get_success_url(self):
        return reverse_lazy('blog-view')

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['title'] = self.object.titulo + ' - Eliminar Post Anconi'
        return data

class CategoriesView(ListView):
    model = Categoria
    template_name = "blog-index.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:3]
        data['categorias'] = Categoria.objects.all()
        data['object'] = Categoria.objects.get(titulo__iexact = self.kwargs['slug'])
        data['search'] = SearchForm
        data['tittle'] = 'Categoria: ' + data['object'].titulo + ' - Anconi Blog'
        return data

    def get_queryset(self, **kwargs):
        categoria = Blog.objects.filter(categoria__titulo__iexact = self.kwargs['slug'])
        return categoria

class BlogSearchView(ListView):
    model = Blog
    template_name = "blog-index.html"
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:3]
        data['categorias'] = Categoria.objects.all()
        data['search'] = SearchForm
        data['busqueda'] = self.request.GET.get('search')
        query = self.request.GET.get('search')
        data['cantidad'] = len(Blog.objects.filter( Q(titulo__icontains =  query) | Q(descripcion__icontains = query) |
                                                    Q(contenido__icontains = query) |  Q(autor__username__icontains = query ) ))
        data['tittle'] = 'Busqueda: ' + data['busqueda'] +' - Blog Anconi'
        return data

    def get_queryset(self, **kwargs):
        query =  self.request.GET.get('search')
        search = Blog.objects.filter( Q(titulo__icontains =  query) | Q(descripcion__icontains = query) |
                                                    Q(contenido__icontains = query) |  Q(autor__username__icontains = query ) )
        search = search.order_by('-fecha')
        return search
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView
from .models import Blog, Categoria
from .forms import BlogCreate
from django.urls import reverse_lazy

# Create your views here.

class BlogHome (ListView):
    model = Blog
    template_name = "blog-index.html"
    ordering = ['-fecha']
    paginate_by = 12
  

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:2]
        data['categorias'] = Categoria.objects.all()

        return data

   


class BlogDetail(DetailView):
    model = Blog
    template_name = "blog-detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = Blog.objects.order_by('-fecha')[:3]
        data['categorias'] = Categoria.objects.all()
        obj = data['object']
        try:
            data["next_obj"] = Blog.get_next_by_fecha(obj)
        except:
            data["next_obj"] = False

        try:
            data["prev_obj"] = Blog.get_previous_by_fecha(obj)
        except:
            data["prev_obj"] = False

        return data



class BlogCreate(CreateView):
    template_name = "blog-create.html"
    model = Blog
    form_class = BlogCreate

    def get_success_url(self):
        return reverse_lazy('blog-detail', args = (self.object.slug, ))

    def form_valid(self, form):
        obj= form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


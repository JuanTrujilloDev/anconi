from django import forms
from .models import Blog

class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['titulo', 'categoria', 'descripcion', 'image', 'contenido']

    #ADDING CLASSES TO FIELDS

    def __init__(self, *args, **kwargs):
        super(BlogCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_titulo(self, *args, **kwargs):
        instance = self.instance
        titulo = self.cleaned_data.get('titulo')
        qs = Blog.objects.filter(titulo__iexact = titulo)
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        if qs.exists():
            raise forms.ValidationError("El titulo ya esta siendo utilizado, por favor seleccione otro.")
        return titulo

class SearchForm(forms.Form):
    search = forms.CharField(label='',  max_length= 30)

    def clean_search(self, *args, **kwargs):
        data = self.cleaned_data.get('search')
        data = data.translate ({ord(c): " " for c in "!@#$^&*()[]}{;:,./<>?\|'`+="})
        return data
    
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = 'Que estas buscando...?'
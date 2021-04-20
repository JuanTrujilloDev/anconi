from django import forms
from .models import Portafolio

class CreateProduct(forms.ModelForm):

    class Meta:
        model = Portafolio
        fields = ['titulo', 'descripcion', 'categoria', 'image']

    
    def __init__(self, *args, **kwargs):
        super(CreateProduct, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_titulo(self, *args, **kwargs):
        instance = self.instance
        titulo = self.cleaned_data.get('titulo')
        qs = Portafolio.objects.filter(titulo__iexact = titulo)
        if instance is not None:
            qs = qs.exclude(pk = instance.pk)
        if qs.exists():
            raise forms.ValidationError("El titulo ya esta siendo utilizado, por favor seleccione otro.")
        return titulo
from django import forms
from .models import Blog

class BlogCreate(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['titulo', 'categoria', 'descripcion','image', 'contenido']

    #ADDING CLASSES TO FIELDS

    def __init__(self, *args, **kwargs):
        super(BlogCreate, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
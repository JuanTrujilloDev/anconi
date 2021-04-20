from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import FileExtensionValidator

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(null=False, blank=False, default="Blog", max_length=15)
    created = models.DateTimeField(auto_now=True, blank= False, null= False)
    slug = models.SlugField(blank= True, null = True, unique=True)

    def get_absolute_url(self):
        return reverse("category-view", kwargs={"slug": self.slug})
    

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save()

        self.slug = slugify(self.titulo)

        super(Categoria, self).save(*args, **kwargs)

class Blog(models.Model):
    categoria = ForeignKey(Categoria, on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 40, blank= False, null = False, verbose_name= "Titulo")
    descripcion = models.CharField(max_length= 150, blank= False, null = False, verbose_name= "Descripcion")
    contenido = models.TextField( blank= False, null = False, verbose_name= "Contenido")
    image = models.ImageField(upload_to = "blog", verbose_name= "Imagen",
    validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png']) ])
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= "Autor")
    fecha = models.DateTimeField(auto_now=True, null = False, blank = False, verbose_name="Fecha Publicacion")
    slug = models.SlugField(unique= True, null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering= ["-fecha"]

    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        super().save()

        im = Image.open(self.image.path)
        im = im.resize((1920, 1080))
        im.thumbnail((960, 540))
        im.save(self.image.path)



        self.slug = slugify(self.titulo)
        self.slug += "-"+slugify(self.pk)

        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog-detail', args = (self.slug, ))
    

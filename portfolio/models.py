from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from io import BytesIO
from django.urls import reverse
from django.core.validators import FileExtensionValidator
# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField( max_length= 20)
    created = models.DateTimeField(auto_now= True, blank= False, null= False)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        super().save()
        self.slug = slugify(self.titulo)
        self.slug += "-"+slugify(self.pk)

        super(Categoria, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return None
    


class Portafolio(models.Model):
    titulo = models.CharField(max_length= 25)
    descripcion = models.TextField(max_length=250)
    image = models.ImageField(upload_to = "portafolio", verbose_name= "Imagen",
    validators = [FileExtensionValidator(allowed_extensions=['jpg', 'png']) ])
    categoria = models.ForeignKey(Categoria, null= False, blank= False, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now= True)
    slug = models.SlugField(null= True, blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-fecha"]

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

        super(Portafolio, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("portfolio-detail", kwargs={"slug": self.slug})
    

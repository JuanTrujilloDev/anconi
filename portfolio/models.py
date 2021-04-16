from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from io import BytesIO

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField( max_length= 20)
    created = models.DateTimeField(auto_now= True, blank= False, null= False)

    def __str__(self):
        return self.titulo


class Portafolio(models.Model):
    titulo = models.CharField(max_length= 25)
    descripcion = models.CharField(max_length=250)
    image = ImageField(null = False, blank = False, upload_to = "portafolio", default="portafolio/default.png")
    categoria = models.ForeignKey(Categoria, null= False, blank= False, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now= True)
    slug = models.SlugField(null= True, blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-fecha"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((1920, 1080))
        im.thumbnail((1920,1080))

        im.save(output, format='PNG', quality = 100)
        output.seek(0)

        super(Portafolio, self).save()

        self.slug = slugify(self.titulo)
        self.slug += "-"+slugify(self.pk)

        super(Portafolio, self).save(*args, **kwargs)

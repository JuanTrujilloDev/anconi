from django.contrib import admin
from .models import Blog, Categoria
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", "slug")
    list_display = ("titulo", "categoria", "fecha")
    ordering = ("categoria", "fecha")
    search_fields = ("titulo", "categoria__titulo")
    date_hierarchy = "fecha"

    list_filter = ("categoria__titulo", "fecha")

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

admin.site.register(Blog, BlogAdmin)
admin.site.register(Categoria, CategoriaAdmin)

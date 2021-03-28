
from django.urls import path
from .views import blogHome, blogDetail, blogCreate

urlpatterns = [
    path('', blogHome, name="blog-view"),
    path('detail', blogDetail, name="blog-detail"),
    path('create', blogCreate, name="blog-create"),
]

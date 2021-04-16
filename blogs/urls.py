
from django.urls import path
from .views import BlogHome, BlogDetail, BlogCreate

urlpatterns = [
    path('', BlogHome.as_view() , name="blog-view"),
    path('detail/<slug:slug>/', BlogDetail.as_view(), name="blog-detail"),
    path('create/', BlogCreate.as_view(), name="blog-create"),
]

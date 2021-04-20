
from django.urls import path
from .views import (BlogHome, BlogDetail, BlogCreate, BlogEdit, BlogDelete, BlogSearchView, 
CategoriesView , BlogSearchView)

urlpatterns = [
    path('', BlogHome.as_view() , name="blog-view"),
    path('detail/<slug:slug>/', BlogDetail.as_view(), name="blog-detail"),
    path('update/<slug:slug>/', BlogEdit.as_view(), name="blog-update"),
    path('delete/<slug:slug>/', BlogDelete.as_view(), name="blog-delete"),
    path('category/<slug:slug>/', CategoriesView.as_view(), name="category-view"),
    path('search/', BlogSearchView.as_view(), name="blog-search"),
    path('create/', BlogCreate.as_view(), name="blog-create"),
]

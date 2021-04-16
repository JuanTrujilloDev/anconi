
from django.urls import path
from .views import portfolio, portfolioCreate, portfolioDetail

urlpatterns = [
    path('', portfolio, name="portfolio-view"),
    path('detail', portfolioDetail, name="portfolio-detail"),
    path('create', portfolioCreate, name="portfolio-create"),

]

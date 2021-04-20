
from django.urls import path
from .views import PortfolioUpdate, PortfolioView, PortfolioCreate, PortfolioDetail

urlpatterns = [
    path('', PortfolioView.as_view(), name="portfolio-view"),
    path('detail/<slug:slug>/', PortfolioDetail.as_view(), name="portfolio-detail"),
    path('update/<slug:slug>/', PortfolioUpdate.as_view(), name="portfolio-update"),
    path('create/', PortfolioCreate.as_view() , name="portfolio-create"),

]

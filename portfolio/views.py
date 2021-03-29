from django.shortcuts import render

# Create your views here.
def portfolio (request):
    return render(request, 'portfolio-index.html')

def portfolioCreate(request):

    return render(request, 'portfolio-create.html')

def portfolioDetail(request):

    return render(request, 'portfolio-detail.html')
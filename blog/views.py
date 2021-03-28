from django.shortcuts import render

# Create your views here.

def blogHome (request):


    return render(request, 'blog-index.html')


def blogDetail(request):

    return render(request, 'blog-detail.html')



def blogCreate(request):

    return render(request, 'blog-create.html')

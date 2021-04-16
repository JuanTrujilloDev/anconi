from django.shortcuts import render

# Create your views here.

def login (request):

    return render(request, 'login.html')

def edit(request):
    return render(request, 'edit-profile.html')

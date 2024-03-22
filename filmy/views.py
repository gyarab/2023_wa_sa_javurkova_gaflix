from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def druhy(request):
    return render(request, 'druhy.html')

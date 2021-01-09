from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')

def single(request):
    return render(request, 'mainapp/single.html')

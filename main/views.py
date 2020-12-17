from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def map_show(request):
    return render(request, 'main/map.html')

from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "novaapp/index.html")


def sobre_view(request):
    return render(request, "novaapp/sobre.html")


def interesses_view(request):
    return render(request, "novaapp/interesses.html")
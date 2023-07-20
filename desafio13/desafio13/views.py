from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def acerca_de(request):
    template_name = 'acerca_de.html'
    return render(request,template_name)

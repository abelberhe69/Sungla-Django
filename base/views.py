from django.shortcuts import render, HttpResponse
from .models import Glasses, About, client
# Create your views here.
def homepage(request):
    context  = {
        'about' : About.objects.all(),
        'glasses' : Glasses.objects.all(),
        'client1' : client.objects.get(id=1),
        'client2' : client.objects.get(id=2),
        'client3' : client.objects.get(id=3),
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'about' : About.objects.all()
    }
    return render(request, 'about.html', context)

def glasses(request):
    context = {
        'glasses' : Glasses.objects.all(),
        'about' : About.objects.all()
    }
    return render(request, 'glasses.html', context)

def shop(request):
    context = {
        'about' : About.objects.all(),
    }
    return render(request, 'shop.html',context)

def contact(request):
    context = {
        'about' : About.objects.all(),
    }
    return render(request, 'contact.html', context)
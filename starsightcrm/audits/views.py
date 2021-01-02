from django.shortcuts import render
from .models import Client

# Create your views here.

def index(request):
    return render(request, 'audits/index.html')


def client(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'audits/client.html', context)


def clientDetail(request, pk):
    client = Client.objects.get(id=pk)
    context = {'client':client}
    return render(request, 'audits/detail.html', context)   

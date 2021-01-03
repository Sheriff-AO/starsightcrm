from django.shortcuts import render
from .models import *

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
    sites = Site.objects.filter(client=client)
    total_site = Site.objects.filter(client=client).count()
    context = {
        'client':client,
        'sites': sites,
        'total_site': total_site
        }
    return render(request, 'audits/detail.html', context) 


def allSite(request):
    sites = Site.objects.all()
    context = {
        'sites': sites
    }
    return render(request, 'audits/site.html', context)  

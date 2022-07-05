
from django.shortcuts import render

from app.crm.models import Client

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class ClientListView(ListView):
    model = Client

class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    
    success_url = reverse_lazy('crm:client_list')

class ClientDetailView(DetailView):
    model = Client

class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    
    success_url = reverse_lazy('crm:client_list')

class ClientDeleteView(DeleteView):
    model = Client
    fields = "__all__"
    
    success_url = reverse_lazy('crm:client_list')
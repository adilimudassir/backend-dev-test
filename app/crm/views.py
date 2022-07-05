
from django.shortcuts import render

from app.crm.models import Client

from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.

# def home():
#     return redirect("crm:client_list")

class ClientListView(ListView):
    model = Client
    template_name = "clients/list.html"

class ClientCreateView(CreateView):
    model = Client
    fields = "__all__"
    template_name = "clients/form.html"
    success_url = reverse_lazy("crm:client_list")

class ClientDetailView(DetailView):
    model = Client
    template_name = "clients/detail.html"


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"
    template_name = "clients/form.html"
    success_url = reverse_lazy("crm:client_list")

class ClientDeleteView(DeleteView):
    model = Client
    fields = "__all__"
    template_name = "clients/confirm_delete.html"
    
    success_url = reverse_lazy("crm:client_list")
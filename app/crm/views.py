
from django.shortcuts import render

from app.crm.models import Client, ClientWallet
from app.crm.forms import AddClientForm, ClientWalletForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import FormView
from django.views.generic.edit import DeleteView

# Create your views here.

# def home():
#     return redirect("clients:client_list")

# class ClientListView(ListView):
#     model = Client
#     template_name = "clients/list.html"

# class ClientCreateView(CreateView):
#     # model = Client
#     # fields = "__all__"
#     form_class = AddClientForm
#     template_name = "clients/form.html"
#     success_url = reverse_lazy("clients:client_list")

# class ClientDetailView(DetailView):
#     model = Client
#     template_name = "clients/detail.html"

# class ClientUpdateView(UpdateView):
#     model = Client
#     fields = "__all__"
#     template_name = "clients/form.html"
#     success_url = reverse_lazy("clients:client_list")

# class ClientDeleteView(DeleteView):
#     model = Client
#     fields = "__all__"
#     template_name = "clients/confirm_delete.html"
    
#     success_url = reverse_lazy("clients:client_list")

def client_index(request):
    clients = Client.objects.all()

    context = {
        "clients": clients,
    }
    return render(request, "clients/index.html", context)

def client_detail(request, pk):
    client = Client.objects.get(pk=pk)

    context = {
        "client": client,
    }
    return render(request, "clients/detail.html", context)

def client_create(request):
    if request.method == "POST":
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            #add client to wallet
            wallet = ClientWallet.objects.create(client=form.instance)
            return redirect("clients:client_list")
        # client = Client.objects.create(
        #     cid = request.POST["cid"],
        #     first_name = request.POST["first_name"],
        #     last_name = request.POST["last_name"],
        #     email = request.POST["email"],
        #     phone = request.POST["phone"],
        #     country_code = request.POST["country_code"],
        #     address = request.POST["address"],
        # )
        # return redirect("clients:client_detail", pk=client.pk)
    else:
        form = AddClientForm()
    context = {
        "form": form,
    }
    return render(request, "clients/form.html", context)

def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    if request.method == "POST":
        form = AddClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("clients:client_list")
    else:
        form = AddClientForm(instance=client)
    context = {
        "form": form,
        "client": client,
    }
    return render(request, "clients/form.html", context)

def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    # if request.method == "POST":
    #delete client wallet first
    client_wallet = ClientWallet.objects.get(client=client)
    client_wallet.delete()

    #delete client
    client.delete()
    return redirect("clients:client_list")
    # context = {
    #     "client": client,
    # }
    # return render(request, "clients/confirm_delete.html", context)


def client_wallet_update(request, pk):
    client_wallet = ClientWallet.objects.get(pk=pk)
    if request.method == "POST":
        form = ClientWalletForm(request.POST, instance=client_wallet)
        if form.is_valid():
            form.save()
            return redirect("clients:client_detail", pk=client_wallet.client.pk)
    else:
        form = ClientWalletForm(instance=client_wallet)
    context = {
        "form": form,
    }
    return render(request, "clients/wallet_form.html", context)

from django.shortcuts import render
from django.contrib import messages

from app.crm.models import Client, ClientWallet
from app.crm.forms import ClientForm, ClientWalletForm
from django.shortcuts import redirect


def client_index(request):
    clients = Client.objects.all()

    return render(request, "clients/index.html", {
        "clients": clients,
    })

def client_detail(request, pk):
    client = Client.objects.get(pk=pk)

    return render(request, "clients/detail.html", {
        "client": client,
    })

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        
        if form.is_valid():
            form.save()

            #add client to wallet
            ClientWallet.objects.create(client=form.instance)
            
            messages.success(request, "Client created successfully")
            return redirect("clients:client_list")
        else:
            messages.error(request, "Error creating client")
    
    else:
        form = ClientForm()
    
    return render(request, "clients/form.html", {
        "form": form
    })

def client_update(request, pk):
    client = Client.objects.get(pk=pk)
    
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Client updated successfully")
            return redirect("clients:client_detail", pk=client.pk)
        else:
            messages.error(request, "Error updating client")

    else:
        form = ClientForm(instance=client)
    
    return render(request, "clients/form.html", {
        "form": form,
        "client": client,
    })

def client_delete(request, pk):
    client = Client.objects.get(pk=pk)
    #delete client wallet first
    client_wallet = ClientWallet.objects.get(client=client)
    client_wallet.delete()

    #delete client
    client.delete()

    messages.success(request, "Client deleted successfully")
    return redirect("clients:client_list")


def client_wallet_update(request, pk):
    client_wallet = ClientWallet.objects.get(pk=pk)
    
    if request.method == "POST":
        form = ClientWalletForm(request.POST, instance=client_wallet)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Client wallet updated successfully")
            return redirect("clients:client_detail", pk=client_wallet.client.pk)
        else:
            messages.error(request, "Error updating client wallet")
    
    else:
        form = ClientWalletForm(instance=client_wallet)

    return render(request, "clients/wallet_form.html", {
        "form": form
    })
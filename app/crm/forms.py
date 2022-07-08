
from django import forms
from .models import Client, ClientWallet


class ClientForm(forms.ModelForm):
    cid = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Client ID",
            }
        ),
        label = "Client ID",
        required = True,
    )
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "First Name",
            }
        )
    )
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Last Name",
            }
        )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Email",
            }
        )
    )
    phone = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Phone",
            }
        )
    )
    address = forms.CharField(
        widget = forms.Textarea(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Address",
            }
        )
    )
    country_code = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Country Code",
            }
        )
    )



    class Meta:
        model = Client
        fields = ('cid', 'first_name', 'last_name', 'country_code', 'email', 'address', 'phone')

class ClientWalletForm(forms.ModelForm):
    total_balance = forms.DecimalField(
        widget = forms.NumberInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Total Balance",
            }
        )
    )
    available_balance = forms.DecimalField(
        widget = forms.NumberInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Available Balance",
            }
        )
    )
    lien_balance = forms.DecimalField(
        widget = forms.NumberInput(
            attrs = {
                "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                "placeholder": "Lien Balance",
            }
        )
    )
    class Meta:
        model = ClientWallet
        fields = ('total_balance', 'available_balance', 'lien_balance')
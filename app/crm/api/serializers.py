from rest_framework import serializers
from app.crm.models import Client, ClientWallet

class ClientWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWallet
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    clientwallet = ClientWalletSerializer(read_only=True)
    
    class Meta:
        model = Client
        fields = (
            'id',
            'cid',
            'first_name',
            'last_name',
            'country_code',
            'email',
            'address',
            'phone',
            'created',
            'updated',
            'clientwallet',
        )

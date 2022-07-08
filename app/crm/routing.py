from django.urls import re_path
from app.crm.consumers import ClientWalletConsumer

websocket_urlpatterns = [
    re_path(r'ws/client_wallet/(?P<wallet_id>\w+)/$', ClientWalletConsumer.as_asgi())
]
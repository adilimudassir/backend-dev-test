import json
from channels.generic.websocket import WebsocketConsumer

class ClientWalletConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'success',
            'message': 'You are connected'
        }))
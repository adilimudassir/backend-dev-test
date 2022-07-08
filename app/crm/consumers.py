import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ClientWalletConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope["url_route"]["kwargs"]["wallet_id"]

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type': "wallet_update",
                'message': text_data_json
            }
        )

    def wallet_update(self, event):
        self.send(text_data=json.dumps({
            'type': 'update',
            'message': event['message']
        }))
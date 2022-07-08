from distutils.command.clean import clean
from urllib import response
import requests

from app.crm.models import Client, ClientWallet

class ClientJobs:
    def fetch_clients():
        link = f"https://62c2c06cff594c656764970a.mockapi.io/users"

        response = requests.get(link)
        
        if response.status_code == 200:
            result = response.json()

            for client in result['data']:
                
                try:
                    Client.objects.get(cid=client['cid'])
                except Client.DoesNotExist:
                    instance = Client.objects.create(
                        cid = client["cid"],
                        first_name = client["first_name"],
                        last_name = client["last_name"],
                        email = client["email"],
                        phone = client["phone"],
                        country_code = client["country_code"],
                        address = client["address"],
                        id = client["id"],
                        created = client["created_at"],
                    )
                    
                    #add client to wallet
                    ClientWallet.objects.create(client=instance)
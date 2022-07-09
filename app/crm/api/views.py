from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.crm.models import Client
from app.crm.api.serializers import ClientSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        'GET /api',
        'GET /api/clients',
        'GET /api/clients/<int:id>',
    ]

    return Response(routes)

@api_view(['GET'])
def clients(request):
    clients = Client.objects.select_related('clientwallet').all()
    serializer = ClientSerializer(clients, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_client(request, pk):
    clients = Client.objects.select_related('clientwallet').get(pk=pk)
    serializer = ClientSerializer(clients, many=False)

    return Response(serializer.data)

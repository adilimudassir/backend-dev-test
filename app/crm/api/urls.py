from django.urls import path
from app.crm.api import views

urlpatterns = [
    path("", views.get_routes),
    path("clients", views.clients),
    path("clients/<int:pk>", views.get_client)
]
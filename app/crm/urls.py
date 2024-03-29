from django.urls import path
from . import views

app_name = 'app.crm'

urlpatterns = [
    path("", views.client_index, name="client_list"),
    path("create/", views.client_create, name="client_create"),
    path("<int:pk>/", views.client_detail, name="client_detail"),
    path("<int:pk>/update/", views.client_update, name="client_update"),
    path("<int:pk>/delete/", views.client_delete, name="client_delete"),
    path("<int:pk>/wallet/update", views.client_wallet_update, name="client_wallet_update"),
]
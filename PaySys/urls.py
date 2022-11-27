from django.urls import path

from PaySys.views import *

app_name = "paysys"

urlpatterns = [
    path('buy/', api_get_buyItem, name='buyItemId'),
    path('item/<int:id>/', viewItem, name='viewItemId'),
    path('catalog/', viewCatalog, name='viewItemId'),
    path('config/', stripe_config),
    path('webhook/', stripe_webhook),
    path('success/', success_stripe),
    path('cancelled/', cancelled_stripe),
]
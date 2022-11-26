from django.urls import path

from PaySys.views import *

app_name = "paysys"

urlpatterns = [
    path('buy/<int:id>', api_post_buyItem, name='buyItemId'),
    path('item/<int:id>', api_get_viewItem, name='viewItemId'),
    path('config/', stripe_config),
    path('webhook/', stripe_webhook),
    path('success/', success_stripe),
    path('cancelled/', cancelled_stripe),
]
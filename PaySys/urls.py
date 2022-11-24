from django.urls import path

from PaySys.views import *

app_name = "paysys"

urlpatterns = [
    path('', home_page, name='home'),
    path('config/', stripe_config),
    path('create-checkout-session/', create_checkout_session),
    path('success/', success_stripe),
    path('cancelled/', cancelled_stripe),
    path('webhook/', stripe_webhook),

    path('buy/<int:id>', api_post_buyItem, name='buyItemId'),
    path('item/<int:id>', api_get_viewItem, name='viewItemId'),
]
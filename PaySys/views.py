import os

import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from PaySys.models import Item


def api_post_buyItem(request, id):
    item = Item.objects.get(id=id)

    domain_url = os.getenv('DOMAIN_URL', 'http://localhost:8000/')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    # 'currency': 'usd',
                    # 'unit_amount': 150,
                    'currency': str(item.currency),
                    'unit_amount': int(item.price) * 100,
                    'product_data': {
                        # 'name': 'test product',
                        # 'description': 'it\'s my first test product',
                        'name': str(item.name),
                        'description': str(item.description),
                        'images': [],
                    },
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
        )
    except Exception as er:
        return JsonResponse({'error': str(er)})
    return JsonResponse({'id': checkout_session['id']})


def api_get_viewItem(request, id):
    item_info = {'id': id, 'name': '', 'description': '', 'price': '', 'currency': ''}
    try:
        item = Item.objects.get(id=id)
        item_info['name'] = item.name
        item_info['description'] = item.description
        item_info['price'] = item.price
        item_info['currency'] = item.currency
    except Exception as er:
        error_message = f"Item with id={id} does not exist"
        return render(request, 'PaySys/error.html', context={'error': error_message})

    return render(request, 'PaySys/view_info_item.html', context={'Item': item_info})


def success_stripe(request):
    return render(request, 'PaySys/success.html')


def cancelled_stripe(request):
    return render(request, 'PaySys/cancelled.html')


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_conf = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_conf, safe=False)


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)


    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
    else:
        print("type event - ", event['type'])

    return HttpResponse(status=200)

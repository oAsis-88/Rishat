import os

import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from PaySys.models import *


def api_get_buyItem(request):
    items = {}
    currency_order = "USD"
    for key, value in request.GET.items():
        if key == 'currency':
            currency_order = value
        else:
            items[key] = value
    sum_price_items = 0
    metadata = {}
    description_line_items = ""  # 1 RUB = 60 USD;
    tax_usd = 0
    tax_rub = 0
    taxs_id = []
    # discount_id = []  # Пока не добавлено
    last_item = Order.objects.last()
    new_order_id = last_item.id + 1 if last_item else 1
    order = Order.objects.create(name=f"Заказ №{new_order_id}")

    for key, value in items.items():
        count_item = int(value)
        item = Item.objects.get(id=int(key))
        OrderItems.objects.create(item=item, order=order, count=count_item)
        currency = item.currency

        if tax_rub == 0 and currency == "RUB":
            tax_rub = Tax.objects.get(name="НДС")
            taxs_id.append(tax_rub.id)
        if tax_usd == 0 and currency == "USD":
            tax_usd = Tax.objects.get(name="VAT")
            taxs_id.append(tax_usd.id)

        price_item = item.price * count_item
        if currency_order == "USD" and currency == "RUB":
            price_item = round(price_item / 60, 2)
        if currency_order == "RUB" and currency == "USD":
            price_item = price_item * 60

        sum_price_items += price_item

        description_line_items += f" {item.name} - {count_item}шт; "

        metadata[f'description_{item.id}'] = item.description
        metadata[f'price_{item.id}'] = str(price_item) + " USD"
        metadata[f'count_{item.id}'] = count_item
        metadata[f'tax_{item.id}'] = "{}%".format(tax_rub.percent if currency == "RUB" else tax_usd.percent)

    order = Order.objects.get(name=f"Заказ №{new_order_id}")
    for tax_id in taxs_id:
        order.tax.add(tax_id)

    domain_url = os.getenv('DOMAIN_URL', 'http://localhost:8000/')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': currency_order,
                    'unit_amount': int(sum_price_items * 100),
                    'product_data': {
                        'name': order.name,
                        'description': description_line_items,
                        'images': [],
                    },
                },
                'quantity': 1,
            }],
            metadata=metadata,
            payment_intent_data={
                "metadata": {
                    "test": "TEST_TEXT",
                }
            },
            mode='payment',
            success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + 'cancelled/',
        )
    except Exception as er:
        return JsonResponse({'error': str(er)})
    return JsonResponse({'id': checkout_session['id']})


def viewItem(request, id):
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


def viewCatalog(request):
    items = Item.objects.all()
    return render(request, 'PaySys/view_catalog_items.html', context={'Items': items})


def add_to_cart(request):
    items = Item.objects.all()
    return render(request, 'PaySys/view_catalog_items.html', context={'Items': items})


def viewCart(request):
    items = Item.objects.all()
    return render(request, 'PaySys/view_cart.html', context={'Items': items})


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

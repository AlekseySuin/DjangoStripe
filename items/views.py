from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Item
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data':{
                'currency': 'usd',
                'product_data': {
                    'name':item.name,
                },
                'unit_amount':item.price,
            },
            'quantity':1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return JsonResponse({'session_id':session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item_detail.html',{
        'item':item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })
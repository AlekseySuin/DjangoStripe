from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import Item, Order
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def order_checkout_session(request, id):
    try:
        order = get_object_or_404(Order, id=id)

        items = []
        for item in order.items.all():
            items.append({
                'price_data':{
                    'currency': 'usd',
                    'product_data': {
                        'name':item.name,
                    },
                    'unit_amount':item.price_in_dollars(),
                },
                'quantity':1,
            })
        discounts = []
        if order.discount:
            discounts.append({
                'coupon': stripe.Coupon.create(
                    percent_off=order.discount.amount,
                    duration="once",
                ).id
            })

        tax_rates = []
        if order.tax:
            tax_rates.append(
                stripe.TaxRate.create(
                    display_name=order.tax.description,
                    percentage=order.tax.rate,
                    inclusive=False,
                ).id
            )
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            discounts=discounts,
            tax_rates=tax_rates,
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
        return JsonResponse({'session_id': session.id})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)

    price_in_dollars = item.price_in_dollars()

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data':{
                'currency': 'usd',
                'product_data': {
                    'name':item.name,
                },
                'unit_amount':price_in_dollars,
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

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'order_detail.html',{
        'order':order,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    })

def items_get(request):
    items = Item.objects.all()
    return render(request, 'items_list.html', {
        'items': items,
    })

def orders_get(request):
    orders = Order.objects.all()
    return render(request, 'orders_list.html', {
        'orders': orders,
    })
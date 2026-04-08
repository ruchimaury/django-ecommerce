from django.shortcuts import render, redirect
from .models import Order

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def home(request):
    products = [
        {"name": "Product 1", "price": 100},
        {"name": "Product 2", "price": 200},
        {"name": "Product 3", "price": 300},
    ]

    orders = Order.objects.filter(is_paid=True)

    return render(request, "home.html", {
        "products": products,
        "orders": orders
    })

def buy(request):
    if request.method == "POST":
        name = request.POST['name']
        price = int(request.POST['price'])
        qty = int(request.POST['qty'])


        order = Order.objects.create(
            product_name=name,
            quantity=qty,
            amount=price * qty
        )


        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {'name': name},
                    'unit_amount': price * 100,
                },
                'quantity': qty,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success/' + str(order.id),
            cancel_url='http://127.0.0.1:8000/',
        )

        return redirect(session.url)

    return redirect('/')



def success(request, order_id):
    order = Order.objects.get(id=order_id)
    if not order.is_paid:
        order.is_paid = True
        order.save()

    return redirect('/')




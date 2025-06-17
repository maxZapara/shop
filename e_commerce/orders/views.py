from django.shortcuts import render

# Create your views here.


def create_order(request):
    from .forms import OrderForm
    from core.cart import Cart
    from core.models import Product
    from django.shortcuts import get_object_or_404
    from .models import OrderItem
    from django.contrib import messages
    from django.contrib.auth.models import User
    

    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            order=form.save()
            cart=Cart(request)
            cart_items=cart.get_cart()
            for (product_id, info) in cart_items.items():
                p=get_object_or_404(Product, id=product_id)
                order_item=OrderItem(order=order, product=p, quantity=info.get("quantity",1))
                order_item.save()
                
            order.calculate_total_price()
            order.save()

            admins=User.objects.filter(is_staff=True, is_superuser=True).all()
            print("Admins to call: ", admins)

            messages.success(request, "Thanks for your order!")

            cart.clear()
            form=OrderForm()

    else:
        form=OrderForm()


    return render(request, "orders/create_order.html", {"form":form})
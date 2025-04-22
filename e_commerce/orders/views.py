from django.shortcuts import render

# Create your views here.


def create_order(request):
    return render(request, "core/create_order.html")
from django.shortcuts import render

# Create your views here.

def home(request):
    from .models import Product

    products=Product.objects.all()

    return render(request, 'core/index.html', {'products': products})

def product_details(request, id):
    from django.shortcuts import get_object_or_404
    from .models import Product
    from .forms import CommentForm

    product=get_object_or_404(Product, id=id)
    product_gallery=product.gallery.all()
    
    comment_form=CommentForm()
    return render(request, 'core/contentDetails.html', {'product':product, 'gallery':product_gallery, 'comment_form':comment_form})


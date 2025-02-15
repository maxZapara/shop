from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    from .models import Product

    products=Product.objects.all()

    return render(request, 'core/index.html', {'products': products})

@login_required
def product_details(request, id):
    from django.shortcuts import get_object_or_404
    from .models import Product
    from .forms import CommentForm

    product=get_object_or_404(Product, id=id)
    product_gallery=product.gallery.all()
    
    if request.method == 'POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.product=product
            comment.author=request.user
            comment.save()


    else:
        comment_form=CommentForm()

    product_comment=product.comments.all()
    print(product_comment)

    return render(request, 'core/contentDetails.html', {'product':product, 'gallery':product_gallery, 'comment_form':comment_form, 'product_comment':product_comment})

@csrf_exempt
# @login_required
def delete_comment(request, comment_id):
    from .models import Comment
    from django.shortcuts import get_object_or_404
    from django.http import JsonResponse


    if request.method == 'DELETE':
        comment=get_object_or_404(Comment, id=comment_id)
        # if comment.author != request.user:
        #     return JsonResponse({'success' : False, 'message': 'You can delete only your comment'}, status=400)
        comment.delete()
        return JsonResponse({'success' : True})
    
    return JsonResponse({'success' : False, 'message': 'Invalid metod'}, status=400)

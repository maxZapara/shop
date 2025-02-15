from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    icon = models.TextField(null=True, blank=True, default="""<svg viewBox="-0.5 0 25 25" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M19 3.32001H16C14.8954 3.32001 14 4.21544 14 5.32001V8.32001C14 9.42458 14.8954 10.32 16 10.32H19C20.1046 10.32 21 9.42458 21 8.32001V5.32001C21 4.21544 20.1046 3.32001 19 3.32001Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M8 3.32001H5C3.89543 3.32001 3 4.21544 3 5.32001V8.32001C3 9.42458 3.89543 10.32 5 10.32H8C9.10457 10.32 10 9.42458 10 8.32001V5.32001C10 4.21544 9.10457 3.32001 8 3.32001Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M19 14.32H16C14.8954 14.32 14 15.2154 14 16.32V19.32C14 20.4246 14.8954 21.32 16 21.32H19C20.1046 21.32 21 20.4246 21 19.32V16.32C21 15.2154 20.1046 14.32 19 14.32Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M8 14.32H5C3.89543 14.32 3 15.2154 3 16.32V19.32C3 20.4246 3.89543 21.32 5 21.32H8C9.10457 21.32 10 20.4246 10 19.32V16.32C10 15.2154 9.10457 14.32 8 14.32Z" stroke="#000000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>""")
    
    slug=models.SlugField(unique=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Categories"
        ordering=["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title


# Create your models here.
class Product(models.Model):
    category=models.ForeignKey(Category, null=True, related_name="products", on_delete=models.CASCADE)
    title=models.CharField(null=False, blank=False, max_length=250)
    description=models.TextField(null=False, blank=False)
    price=models.DecimalField(null=False, blank=False, default=0.0, decimal_places=2, max_digits=10)
    discount=models.IntegerField()
    available=models.BooleanField(null=False, blank=False, default=True)
    created_at=models.DateTimeField(null=False, blank=False, auto_now_add=True)

    def get_first_image(self):
        gallery_image = self.gallery.last()
        return gallery_image.image.url if gallery_image else None

    def __str__(self):
        return self.title
    def __repr__(self):
        return self.title
    
def gallery_upload_to(instance, filename):
    return f"products/{slugify(instance.product_id)}/{filename}"

class ProductGallery(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery")
    image=models.ImageField(upload_to=gallery_upload_to)


class Comment(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments", null=True)
    content=models.TextField(blank=False, null=False)
    created_at=models.DateTimeField(auto_now_add=True)
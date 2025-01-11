from django.dispatch import receiver
from .models import ProductGallery, Product
from django.db.models.signals import post_delete
import os
from django.utils.text import slugify


@receiver(post_delete, sender=ProductGallery)
def delete_product_gallery_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(post_delete, sender=Product)
def delete_product_images(sender, instance, **kwargs):
    product_folder = os.path.join("products", slugify(instance.title))
    if os.path.isdir(product_folder):
        for file in os.listdir(product_folder):
            file_path = os.path.join(product_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(product_folder)

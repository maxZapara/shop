from django.contrib import admin
from .models import Product, Category, ProductGallery

# Register your models here.
admin.site.register(Category)

class GalleryInlineAdmin(admin.TabularInline):
    model=ProductGallery
    extra=1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'discount','available')
    list_filter = ('category','available')
    search_fields = ('title', 'description')
    list_editable=('price', 'discount', 'available')
    inlines=[GalleryInlineAdmin]

class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
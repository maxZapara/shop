from django.contrib import admin
from .models import Product, Category, ProductGallery, Brand, Size
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import SliderNumericFilter, RangeDateFilter

class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10

# --- Category Admin ---
@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ("title", "slug", "created_at")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)

# --- Brand Admin ---
@admin.register(Brand)
class BrandAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

# --- Size Admin ---
@admin.register(Size)
class SizeAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)

class ProductSizeInline(TabularInline):
    model = Product.size.through
    extra = 1

class GalleryInlineAdmin(TabularInline):
    model = ProductGallery
    fields = ("product_image",)
    readonly_fields = ("product_image",)
    extra = 1

    def product_image(self, obj):
        from django.utils.html import format_html

        try:
            img = obj.image.url
            return format_html(
                "<img src={} width='100' height='100' style='object-fit:cover;' />", img
            )
        except Exception:
            return "Error"


# --- Product Admin ---
@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "title",
        "category",
        "brand",
        "get_sizes",
        "price",
        "discount",
        "available",
    )
    list_filter = (
        "category",
        "brand",
        "size",
        "available",
        ("price", SliderNumericFilter),
        ("created_at", RangeDateFilter),
    )
    search_fields = ("title", "description")
    list_editable = ("price", "discount", "available")
    inlines = [GalleryInlineAdmin]
    autocomplete_fields = ("category", "brand", "size")

    def get_sizes(self, obj):
        return ", ".join([size.name for size in obj.size.all()])

    get_sizes.short_description = "Sizes"

@admin.register(ProductGallery)
class ProductGalleryAdmin(ModelAdmin):
    list_display = ("product", "image")
from django.contrib import admin
from .models import Order, OrderItem
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import SliderNumericFilter, RangeDateFilter
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm


class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 10

class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 0
    fields = ("product", "product_price", "product_image", "quantity")
    readonly_fields = (
        "product",
        "product_price",
        "quantity",
        "product_image"
    )
    
    def product_image(self,obj):
        from django.utils.html import format_html


        try:
            img=obj.product.get_first_image()
            return format_html(
                "<img src={} width='50' height='50' style='object-fit:cover;' />", img
            )
        except Exception:
            return "Error"

    def product_price(self, obj):
        return obj.product.price if obj.product else "-"

@admin.register(Order)
class OrderAdmin(ModelAdmin, ImportExportModelAdmin):
    export_form_class=ExportForm

    list_display = ("first_name","last_name", "adress","city","state","postal_code","order_notes","total_price","created_at","updated_at","status")
    list_filter = ('status',("total_price", CustomSliderNumericFilter), ("created_at", RangeDateFilter),('updated_at',RangeDateFilter),)
    search_fields = ('city', 'status', 'first_name', 'state')
    list_editable=('status',)
    inlines=[OrderItemInline]



@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ("id", "order", "product", "quantity")
    list_filter = ("order", "product")
    search_fields = ("order__first_name", "order__last_name", "product__name")

# Register your models here.

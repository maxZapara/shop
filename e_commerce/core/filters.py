import django_filters
from .models import Product, Brand, Size, Category
from django import forms

class ProductFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter(label="Ціна")
    brand = django_filters.ModelChoiceFilter(
        queryset=Brand.objects.all(), label="Бренд"
    )
    size = django_filters.ModelMultipleChoiceFilter(
        queryset=Size.objects.all(),
        label="Розмір",
        widget=forms.CheckboxSelectMultiple,
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(), label="Категорія"
    )
    has_discount = django_filters.BooleanFilter(
        label="Є знижка", method="filter_has_discount"
    )

    class Meta:
        model = Product
        fields = ["category", "price", "brand", "size", "has_discount"]

    def filter_has_discount(self, queryset, name, value):
        if value:
            return queryset.filter(discount__gt=0)
        else:
            # return queryset.filter(discount=0)
            return queryset.all()
from django import forms

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "adress",
            "city",
            "postal_code",
            "state",
            "order_notes",
        ]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone":"Phone Number",
            "email":"Email",
            "adress": "Adress",
            "city": "City",
            "postal_code": "Postal Code",
            "state": "State",
            "order_notes": "Order Notes",
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if phone:
            if phone.startswith("+0"):
                raise forms.ValidationError("Phone number can not start with +0.")
            return phone
        raise forms.ValidationError("Phone number must be provided.")
from django.forms import ModelForm
from .models import Products


class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'date_rec', 'price', 'u_measure', 'name_provider']

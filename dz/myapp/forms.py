import datetime

from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField(min_value=0)
    data_product = forms.DateField(initial=datetime.date.today)


class ImageForm(forms.Form):
    image = forms.ImageField()

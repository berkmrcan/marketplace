from django import forms

from .models import Product

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','price','inventory','image')

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','description','price','inventory','image')

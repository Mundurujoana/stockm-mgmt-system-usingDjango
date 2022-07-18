from dataclasses import field
from pyexpat import model
import re
from signal import raise_signal
from unicodedata import category
from django import forms

from .models import Stock

class StockcreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is require')

        for items in Stock.objects.all():
            if items.category == category:
                raise forms.forms.ValidationError(category +" "+ 'is already created')
        return category

    def clean_item_name(self):
            item_name = self.cleaned_data.get('item_name')
            if not item_name:
                raise forms.ValidationError('This field is required')
            for items in Stock.objects.all():
              if items.item_name == item_name:
                  raise forms.forms.ValidationError(item_name +" "+ 'is already created')
            return item_name

class StockSearchForm(forms.ModelForm):
   class Meta:
     model = Stock
     fields = ['category', 'item_name']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
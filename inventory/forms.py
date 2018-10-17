from django import forms
from .models import Item, DatesUsed

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'generic_item_id',
                  'full_quantity',
                  'unit',
                  'expiry_date', 'aeoo_bool',
                  'aeoo_int', 'pack_bool',
                  'pack_int', 'aeoo_date',
                  'barcode', 'indv_barcode',
                  'price', 
                  'item_alert']
        labels = {'item_name': 'Item name'}


#probably not needed
class InputForm(forms.Form):
    intInput = forms.IntegerField(min_value='0')
    labels = {'intInput': ' '}

class UseForm(forms.Form):
    currentQuantity = forms.IntegerField(min_value=0)
    date = forms.DateField()

class DateUseForm(forms.ModelForm):
    currentQuantity = forms.IntegerField(min_value=0)
    class Meta:
        model = DatesUsed
        fields = ['item', 'date']

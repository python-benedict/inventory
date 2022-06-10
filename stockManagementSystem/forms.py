from pyexpat import model
from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity', 'date']

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']

class IssueForm(forms.ModelForm):
        class Meta:
            model = Stock
            fields = ['issue_quantity', 'issue_to']


class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity'] #, 'receive_by'

class ReorderLevelForm(forms.ModelForm):
        class Meta:
            model = Stock
            fields = ['reorder_level']
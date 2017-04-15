from django import forms

from .models import Customer, Account, Transaction
from .widgets import CalendarWidget


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'birthdate')
        widgets = {
            'birthdate': CalendarWidget()
        }


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('customer',)


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'amount', 'description')

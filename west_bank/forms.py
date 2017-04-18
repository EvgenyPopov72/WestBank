from django import forms

from .models import Customer, Account, Transaction
from .widgets import CalendarWidget, CalendarWidget1


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'address', 'birthdate')
        widgets = {
            'birthdate': CalendarWidget1()
        }


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('customer',)


class AddTransactionForm(forms.ModelForm):
    account1 = forms.ModelChoiceField(queryset=Account.objects, label='from account:', empty_label=None)
    account2 = forms.ModelChoiceField(queryset=Account.objects, label='to account:', empty_label=None)

    class Meta:
        model = Transaction
        fields = ('account', 'amount', 'description')


class TransactionBetweenAccountsForm(forms.ModelForm):
    account_from = forms.ModelChoiceField(queryset=Account.objects, label='from account:', empty_label=None)
    account_to = forms.ModelChoiceField(queryset=Account.objects, label='to account:', empty_label=None)
    amount = forms.DecimalField(min_value=0)

    # description = forms.CharField(max_length=200)

    def clean(self):
        cleaned_data = super(TransactionBetweenAccountsForm, self).clean()
        account_from = cleaned_data.get("account_from")
        account_to = cleaned_data.get("account_to")
        amount = cleaned_data.get("amount")
        if account_from.id == account_to.id:
            self.add_error('account_from', 'Accounts is the same')
            self.add_error('account_to', 'Accounts is the same')
        if amount > account_from.balance:
            self.add_error('amount', 'Amount value error!')

    class Meta:
        model = Transaction
        fields = ()


class Deposit_WithdrawTransactionForm(forms.ModelForm):
    OP_TYPE = (
        ('+', 'Deposit'),
        ('-', 'Withdraw'),
    )
    operation_type = forms.CharField(widget=forms.Select(choices=OP_TYPE))

    def __init__(self, *args, **kwargs):
        super(Deposit_WithdrawTransactionForm, self).__init__(*args, **kwargs)
        self.fields['account'].empty_label = None

    def clean(self):
        cleaned_data = super(Deposit_WithdrawTransactionForm, self).clean()
        account = cleaned_data.get("account")
        amount = cleaned_data.get('amount')
        operation_type = cleaned_data.get("operation_type")
        if operation_type == '-':
            cleaned_data['amount'] = -amount

        if account.balance + cleaned_data['amount'] < 0:
            self.add_error('amount', 'Amount value error!')

    class Meta:
        model = Transaction
        fields = ('account', 'amount', 'description')


class FilterTransactionForm(forms.Form):
    filter_by_account = forms.ModelChoiceField(queryset=Account.objects, label='filter by account:', required=False)
    filter_by_date_from = forms.DateTimeField(widget=CalendarWidget, required=False)
    filter_by_date_to = forms.DateField(widget=CalendarWidget, required=False)

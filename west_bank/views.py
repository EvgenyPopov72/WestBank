from django.shortcuts import render, redirect

from .forms import AddCustomerForm, AddAccountForm, AddTransactionForm
from .models import Customer, Account, Transaction


def customers_list(request):
    if request.method == "POST":
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = AddCustomerForm()

    objects = Customer.objects.order_by('name').all()
    return render(request, 'customers_list.html', {'objects': objects, 'form': form})


def accounts_list(request, customer_id=None):
    if request.method == "POST":
        form = AddAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts_list')
    else:
        form = AddAccountForm()

    if customer_id:
        objects = Account.objects.filter(customer=customer_id).order_by('id').all()
        # customer = Customer.objects.get(id=customer_id)
    else:
        objects = Account.objects.order_by('customer__name').all()

    customer = Customer.objects.filter(id=customer_id).all()
    return render(request, 'accounts_list.html', {'objects': objects, 'customer': customer, 'form': form})


def transactions_list(request):
    objects = Transaction.objects.order_by('date').all()
    return render(request, 'transactions_list.html', {'objects': objects})


def transactions_by_account_id(request, account_id):
    objects = Transaction.objects.filter(account=account_id).order_by('date').all()
    account = Account.objects.get(id=account_id)
    return render(request, 'transactions_list.html', {'objects': objects, 'account': account})

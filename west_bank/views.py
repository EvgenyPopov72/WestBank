from django.db.transaction import set_autocommit, commit
from django.shortcuts import render, redirect

from .forms import AddCustomerForm, AddAccountForm, AddTransactionForm, Deposit_WithdrawTransactionForm, \
    TransactionBetweenAccountsForm, FilterTransactionForm
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
        customer = Customer.objects.filter(id=customer_id).all()
    else:
        objects = Account.objects.order_by('customer__name').all()
        customer = Customer.objects.all()

    return render(request, 'accounts_list.html', {'objects': objects, 'customer': customer, 'form': form})


def transactions_list(request, account_id=None):
    if request.method == "POST":
        return redirect('accounts_list')
    else:
        withdraw_form = Deposit_WithdrawTransactionForm()
        acc_transf_form = TransactionBetweenAccountsForm()
        filter_by_account = request.GET.get('filter_by_account')
        filter_by_date_from = request.GET.get('filter_by_date_from')
        filter_by_date_to = request.GET.get('filter_by_date_to')
        filter_form = FilterTransactionForm(request.GET)

    if filter_by_account:
        account_id = filter_by_account
    if account_id:
        objects = Transaction.objects.filter(account_id=account_id).order_by('date')
        account = Account.objects.filter(id=account_id).all()
    else:
        objects = Transaction.objects.order_by('date')
        account = Account.objects.all()

    if filter_by_date_from:
        objects = objects.filter(date__gte=filter_by_date_from)
    if filter_by_date_to:
        objects = objects.filter(date__lte=filter_by_date_to)
    return render(request, 'transactions_list.html', {'objects': objects, 'account': account,
                                                      'withdraw_form': withdraw_form,
                                                      'acc_transf_form': acc_transf_form,
                                                      'filter_form': filter_form})


def transfer_between_account_transaction(request):
    if request.method == "POST":
        acc_transf_form = TransactionBetweenAccountsForm(request.POST)
        if acc_transf_form.is_valid():
            account_from = acc_transf_form.cleaned_data.get('account_from')
            account_to = acc_transf_form.cleaned_data.get('account_to')
            amount = acc_transf_form.cleaned_data.get('amount')

            set_autocommit(False)
            account_from.balance -= amount
            account_from.save()
            account_to.balance += amount
            account_to.save()

            trans_from = Transaction(account=account_from, amount=-amount,
                                     description='Transfer to {} {:04d}'.format(account_to.customer.name,
                                                                                account_to.id))
            trans_from.save()
            trans_to = Transaction(account=account_to, amount=amount,
                                   description='Transfer from {} {:04d}'.format(account_from.customer.name,
                                                                                account_from.id))
            trans_to.save()
            commit()

            return redirect('transactions_list')

        objects = Transaction.objects.order_by('date').all()
        account = Account.objects.all()
        withdraw_form = Deposit_WithdrawTransactionForm()
        return render(request, 'transactions_list.html',
                      {'objects': objects, 'account': account, 'withdraw_form': withdraw_form,
                       'acc_transf_form': acc_transf_form})

    else:
        return redirect('transactions_list')


def deposit_withdraw_transaction(request):
    if request.method == "POST":
        withdraw_form = Deposit_WithdrawTransactionForm(request.POST)
        if withdraw_form.is_valid():
            account = withdraw_form.cleaned_data.get('account')
            amount = withdraw_form.cleaned_data.get('amount')
            op_type = 'Deposit' if withdraw_form.cleaned_data.get('operation_type') == '+' else 'Withdraw'
            descr = withdraw_form.cleaned_data.get('description') or op_type
            account.balance += amount
            account.save()
            obj = withdraw_form.save(commit=False)
            obj.description = descr
            obj.save()
            return redirect('transactions_list')

        objects = Transaction.objects.order_by('date').all()
        account = Account.objects.all()
        acc_transf_form = TransactionBetweenAccountsForm()
        return render(request, 'transactions_list.html',
                      {'objects': objects, 'account': account, 'withdraw_form': withdraw_form,
                       'acc_transf_form': acc_transf_form})

    else:
        return redirect('transactions_list')

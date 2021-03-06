from django.db import models


class Customer(models.Model):
    name = models.CharField('Name of customer', max_length=200)
    address = models.CharField('Address', max_length=200)
    birthdate = models.DateField('Date of birth')

    def __str__(self):
        return self.name


class Account(models.Model):
    customer = models.ForeignKey(Customer, null=False, blank=False, on_delete=models.CASCADE)
    balance = models.DecimalField('Current balance', decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return '{} {:04d} ${:.2f}'.format(self.customer.name, self.id, self.balance)


class Transaction(models.Model):
    account = models.ForeignKey(Account, null=False, blank=False, on_delete=models.CASCADE)
    amount = models.DecimalField('Amount', decimal_places=2, max_digits=10, default=0)
    date = models.DateTimeField('Date of transaction', auto_now_add=True)
    description = models.CharField('Description', max_length=200, blank=True, null=True)

    def __str__(self):
        return '{} ${:.2f} {}'.format(self.account.customer.name, self.amount, self.date)

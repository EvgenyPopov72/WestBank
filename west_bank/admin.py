from django.contrib import admin

from .models import Customer, Transaction, Account

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Transaction)

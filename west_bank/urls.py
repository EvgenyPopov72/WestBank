from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.customers_list, name='home'),
    url(r'^customers_list/$', views.customers_list, name='customers_list'),
    url(r'^accounts_list/(?P<customer_id>[0-9]+)/$', views.accounts_list, name='accounts_by_customer_id'),
    url(r'^accounts_list/$', views.accounts_list, name='accounts_list'),
    url(r'^transactions_list/$', views.transactions_list, name='transactions_list'),
    url(r'^transactions_list/(?P<account_id>[0-9]+)/$', views.transactions_list, name='transactions_by_account_id'),
    url(r'^deposit_withdraw/', views.deposit_withdraw_transaction, name='deposit_withdraw_transaction'),
    url(r'^transfer_bw_accounts/', views.transfer_between_account_transaction, name='transfer_between_account_transaction'),

]
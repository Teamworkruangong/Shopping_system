from django.urls import re_path as url

from . import views

urlpatterns=[
    url(r'^$',views.toOrderView),
    url(r'^toPay/$',views.toPayView),
    url(r'^checkPay/$',views.checkPayView),

]

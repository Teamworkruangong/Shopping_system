from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.toOrderView),
    url(r'^toPay/$',views.toPayView),
    url(r'^checkPay/$',views.checkPayView),

]

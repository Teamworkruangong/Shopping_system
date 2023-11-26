from django.urls import re_path as url

from . import views

urlpatterns=[
    url(r'^register/$',views.RegisterView.as_view()),
    url(r'^center/$',views.centerView),
    url(r'^login/$',views.LoginView.as_view()),
    url(r'^loadCode/$',views.LoadCodeView.as_view()),
    url(r'^checkCode/$',views.CheckCodeView.as_view()),
    url(r'^logout/$',views.LogOutView.as_view()),
    url(r'^address/$',views.AddressView.as_view()),
    url(r'^loadArea/$',views.loadAreaView),
    url(r'^updateDefaultAddr/$',views.updateDefaultAddrView),


]
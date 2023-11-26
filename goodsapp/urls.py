from django.urls import re_path as url
from . import views

urlpatterns=[
    url(r'^$',views.IndexView.as_view()),
    url(r'^category/(\d+)/$',views.IndexView.as_view()),
    url(r'^category/(\d+)/page/(\d+)/$',views.IndexView.as_view()),
    url(r'^goodsdetails/(\d+)/$',views.DetailView.as_view()),
]
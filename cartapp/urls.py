from django.urls import re_path as url

from . import views


urlpatterns = [

    url(r'^$',views.CartView.as_view()),
    url(r'^queryAll/$',views.CartListView.as_view()),
]
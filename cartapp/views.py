from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from cartapp.cartmanager import getCartManger


class CartView(View):
    def post(self,request):
        #获取用户当前操作类型
        flag = request.POST.get('flag','')

        if flag == 'add':
            cartManagerObj = getCartManger(request)
            cartManagerObj.add(**request.POST.dict())


        return HttpResponseRedirect('/cart/queryAll/')


class CartListView(View):
    def get(self,request):

        #获取cartManager对象
        cartManagerObj = getCartManger(request)
        cartItemList = cartManagerObj.queryAll()

        return render(request,'cart.html',{'cartItemList':cartItemList})
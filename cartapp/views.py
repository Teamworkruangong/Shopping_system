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

        elif flag == 'plus':
            cartManagerObj = getCartManger(request)
            #{'flag':'plus','goodsid':'1',...}
            cartManagerObj.update(step=1,**request.POST.dict())

        elif flag == 'minus':
            cartManagerObj = getCartManger(request)
            # {'flag':'plus','goodsid':'1',...}
            cartManagerObj.update(step=-1, **request.POST.dict())


        return HttpResponseRedirect('/cart/queryAll/')


class CartListView(View):
    def get(self,request):

        #获取cartManager对象
        cartManagerObj = getCartManger(request)
        cartItemList = cartManagerObj.queryAll()

        return render(request,'cart.html',{'cartItemList':cartItemList})
import uuid

import datetime
import jsonpickle
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from cartapp.cartmanager import DBCartManger
from orderapp.models import Order, OrderItem
from userapp.models import Address
from utils.alipay_p3 import AliPay


def toOrderView(request):

    cartitems = request.GET.get('cartitems','')
    # 获取支付总金额
    totalPrice = request.GET.get('totalPrice','')



    #判断当前用户是否登录
    if not request.session.get('user',''):
        # return HttpResponseRedirect('/user/login/?reflag=order&cartitems='+cartitems)
        return render(request,'login.html',{'reflag':'order','cartitems':cartitems,'totalPrice':totalPrice})


    #反序列化cartitems
    #[{'goodsid':1,'sizeid':'2','colorid':'3'},{}]
    cartitemList = jsonpickle.loads(cartitems)


    #获取默认收货地址
    user = jsonpickle.loads(request.session.get('user',''))
    addrObj = user.address_set.get(isdefault=True)

    #获取订单内容
    #[CartItem(),CartItem()]
    cartItemObjList = [DBCartManger(user).get_cartitems(**item) for item in cartitemList if item]

    # toPrice = 0
    # for ci in cartItemObjList:
    #     toPrice += ci.getTotalPrice()


    return render(request,'order.html',{'addrObj':addrObj,'cartItemObjList':cartItemObjList,'totalPrice':totalPrice})


alipayObj = AliPay(appid='2016091100486702', app_notify_url='http://127.0.0.1:8000/order/checkPay/', app_private_key_path='orderapp/keys/my_private_key.txt',
                 alipay_public_key_path='orderapp/keys/alipay_public_key.txt', return_url='http://127.0.0.1:8000/order/checkPay/', debug=True)


def toPayView(request):

    #获取请求参数
    addrid = request.GET.get('address',-1)
    payway = request.GET.get('payway','alipay')
    cartitems = request.GET.get('cartitems','')


    params = {
        'out_trade_num':uuid.uuid4().hex,
        'order_num':datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        'address':Address.objects.get(id=addrid),
        'user':jsonpickle.loads(request.session.get('user', '')),
        'payway':payway
    }



    orderObj = Order.objects.create(**params)

    # '['{'goodsid:1','sizeid:'2',...'}']'
    if cartitems:
        #[{dict1},{dict2}]
        cartitems = jsonpickle.loads(cartitems)

        orderItemList = [OrderItem.objects.create(order=orderObj,**ci) for ci in cartitems if ci]


    urlparam = alipayObj.direct_pay(subject='京东商城', out_trade_no=orderObj.out_trade_num, total_amount=request.GET.get('totalPrice',0))


    url = alipayObj.gateway+'?'+urlparam

    return HttpResponseRedirect(url)


def checkPayView(request):
    #获取所有的请求参数
    params = request.GET.dict()

    #获取签名
    sign = params.pop('sign')

    #进行校验
    if alipayObj.verify(params,sign):
        # 修改订单状态


        #修改库存



        #更新购物车表中数据



        return HttpResponse('支付成功！')

    return HttpResponse('支付失败！')
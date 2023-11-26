import math

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from goodsapp.models import Category, Goods
from django.core.paginator import Paginator


class IndexView(View):
    def get(self,request,categoryid=2,num=1):
        categoryid = int(categoryid)
        num = int(num)

        #1.获取所有的商品类别信息
        categoryList = Category.objects.all().order_by('id')

        #2.获取某个类别下的所有商品信息
        goodsList = Goods.objects.filter(category_id=categoryid).order_by('id')

        #3.添加分页功能
        paginatorObj = Paginator(object_list=goodsList,per_page=8)

        page_goods_obj = paginatorObj.page(num)

        #4.添加页码数
        start = num - math.ceil(10/2)

        if start < 1:
            start = 1

        end = start + 9

        if end > paginatorObj.num_pages:
            end = paginatorObj.num_pages

        if end < 10:
            start = 1
        else:
            start = end - 9

        page_list = range(start,end+1)




        return render(request,'index.html',{'categoryList':categoryList,'goodsList':page_goods_obj,'currentCid':categoryid,'page_list':page_list})


class DetailView(View):
    def get(self,request,goodsid):
        goodsid = int(goodsid)

        #根据商品ID获取商品详情信息
        try:
            goods = Goods.objects.get(id=goodsid)
            return render(request,'detail.html',{'goods':goods})

        except Goods.DoesNotExist:
            return HttpResponse(status=404)
from django.shortcuts import render

# Create your views here.
from django.views import View

from goodsapp.models import Category, Goods


class IndexView(View):
    def get(self,request,categoryid=2):
        categoryid = int(categoryid)

        #1.获取所有的商品类别信息
        categoryList = Category.objects.all().order_by('id')

        #2.获取某个类别下的所有商品信息
        goodsList = Goods.objects.filter(category_id=categoryid)


        return render(request,'index.html',{'categoryList':categoryList,'goodsList':goodsList,'currentCid':categoryid})
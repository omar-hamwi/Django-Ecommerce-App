from django.shortcuts import render 
from django.views import View
from  . models import Product 


def home(request):
    return render(request,"cards/home.html")

def About(request):
    return render(request,"cards/about.html")


def Contact(request):
    return render(request,"cards/contact.html")

class CategoryView(View):
    def get(self,request,val):
        product=Product.objects.filter(category=val)
        title=Product.objects.filter(category=val).values('title')
        return render(request,"cards/category.html",locals())


class categoryTitle(View):
    def get(self,request,val):
        product=Product.objects.filter(title=val)
        title=Product.objects.filter(category=product[0].category).values('title')
        return render(request,"cards/category.html",locals())
    


class ProductDetail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"cards/productdetail.html",locals())
    




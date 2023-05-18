from django.shortcuts import render 
from django.views import View
from  . models import Product ,Customer
from . forms import CustomerRegistrationForm ,CustomerProfileForm
from django.contrib import messages 



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
    

class CustomerRegistrationView(View):
    def get(self,request):
        form =CustomerRegistrationForm()
        return render(request,"cards/customerregistration.html",locals())
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if  form.is_valid():
            form.save()
            messages.success(request,"Congratuluation ! User Register Successfully")
        else:
            messages.warning(request,"Invalid Data Input")
        return render(request,"cards/customerregistration.html",locals())

        
class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request, 'cards/profile.html', locals())

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            mobile=form.cleaned_data['mobile']
            state=form.cleaned_data['state'] 
            zipcode=form.cleaned_data['zipcode']
            reg=Customer(user=user,name=name,locality=locality,mobile=mobile,city=city , state=state , zipcode=zipcode) 
            reg.save()  
            messages.success(request,"congratulations! Profile save successfully ")       
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'cards/profile.html' , locals())
    
def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request,'cards/address.html',locals() )
    
class updateAddress(View):
    def get(self,request,pk):
        add=Customer.objects.get(pk=pk)
        form=CustomerProfileForm(instance=add)
        return render(request,'cards/updateaddress.html',locals() ) 
    def post(self,request,pk):
        form=CustomerProfileForm()
        return render(request,'cards/updateaddress.html',locals() )
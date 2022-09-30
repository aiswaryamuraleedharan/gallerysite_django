from itertools import product
from django.shortcuts import render,redirect
from productadmin.forms import ProductForm
from .models import Product

def Productadmin(request):
    data=Product.objects.all()
    form=ProductForm()
    context={'form':form,'data':data}
    if request.method=='POST':
        form1=ProductForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
    return render(request,'productadmin.html',context)

def Update(request,pk):
    data = Product.objects.get(id=pk)
    form = ProductForm(instance=data)
    context={'form':form}
    if request.method == 'POST':
        form1= ProductForm(request.POST,instance=data)
        if form1.is_valid():    
            form1.save()
            return redirect('/')
    return render(request,'productadmin.html',context)

def DeleteUser(request,pk):
    data = Product.objects.get(id=pk)
    data.delete()
    return redirect('productadmin')

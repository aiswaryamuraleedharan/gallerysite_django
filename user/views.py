from django.shortcuts import render
from productadmin.models import Product

def User(request):
    data=Product.objects.all()
    return render(request,'index.html',{'data':data})

def PaymentPage(request):
    return render(request,'payment.html')

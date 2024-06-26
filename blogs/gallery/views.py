from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm  

# Create your views here.
def product_list(request):
    Products=Product.objects.all()
    return render(request,'templates/index.html',{'products':Product})

def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'templates/index2.html',{'product':Product})

def edit_product(request, pk):
    product=get_object_or_404(Product, pk=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            form=ProductForm(instance=product)
        return render(request,'templates/edit.html',{'form':form})
    
def delete_product(request, pk):
    Product=get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        Product.delete()
        return redirect('product_list')
    return render(request, 'templates/delete.html', {'product':Product})

def home(request):
    return HttpResponse('Hello, World!')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product
from product.forms import ProductForm
from django.http import JsonResponse
from product.serializers import ProductSerializer
from rest_framework.views import APIView


# Create your views here.

def show(request):
    products = Product.objects.all()
    return render(request, "show.html",{'products':products})

def product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = ProductForm()
    return render(request,'add_product.html',{'form':form})

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/show")   

def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit.html',{'product':product})  

def update(request,id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance = product)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'product': product})

def raw_sql(request):
    name = ""
    for p in Product.objects.raw('SELECT * FROM products'):
        name = name + " " + p.pname
    return JsonResponse({'result':name})

def getjson(request):
    return JsonResponse({'name':'broadway'})


def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)

class ProductView(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Product was successfully saved.'})
        return JsonResponse({'message':'unable to save product... '})

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def delete(self, request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse({"message":"product deleted"})   
    

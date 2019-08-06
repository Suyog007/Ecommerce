from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def product_detail(request):  
   template = loader.get_template('product_detail.html')
   return HttpResponse(template.render({"active_tab":"product_detail"})) 
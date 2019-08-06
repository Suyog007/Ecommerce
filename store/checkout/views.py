from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def checkout(request):  
   template = loader.get_template('checkout.html')
   return HttpResponse(template.render({"active_tab":"checkout"})) 
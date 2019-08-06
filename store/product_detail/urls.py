from . import views
from django.urls import path

urlpatterns = [
    path('', views.product_detail, name='product_detail'),
]
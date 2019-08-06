from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('show/', views.show),
    path('add_product/', views.product, name="add_product"),
    path('delete/<int:id>',views.destroy),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>', views.update),
    path('raw_sql/', views.raw_sql),  #to use sql syntax
    path('api/get_products/', views.get_products, name = "get-products"),
    path('api/product', views.ProductView.as_view(), name="product"),
    path('api/product/delete/<int:id>', views.ProductView.as_view(), name="product")

]
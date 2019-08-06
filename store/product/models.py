from django.db import models

# Create your models here.
#every models(color,product and so on) will have seperate tables
class Color(models.Model):
    color=models.CharField(max_length=20,default="white")

class Size(models.Model):
    size=models.CharField(max_length=10,default="M")

class Image(models.Model):
    image=models.ImageField(upload_to='product_images/')

class Product(models.Model):
    pid = models.CharField(max_length=20)
    pname = models.CharField(max_length=100)
    pprice = models.IntegerField()
    prating=models.IntegerField(default=0)
    pshort_description=models.CharField(max_length=300,default="")
    plong_description=models.CharField(max_length=2000,default="")
    pmanufacturer=models.CharField(max_length=2000,default="")
   
    pcolor=models.ForeignKey(Color,on_delete=models.CASCADE,default=1)
    psize=models.ForeignKey(Size,on_delete=models.CASCADE,default=1)
    pimage=models.ForeignKey(Image,on_delete=models.CASCADE,default=None)
    class Meta:
        db_table = "products"

class Payment(models.Model):
    customer_id = models.CharField(max_length=28)
    amount = models.IntegerField()
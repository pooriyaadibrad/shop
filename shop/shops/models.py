from django.db import models
import datetime
# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class customer(models.Model):
    name = models.CharField(max_length=30)
    family=models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name} {self.family}'


class product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='',blank=True,null=True)
    price = models.DecimalField(default=0,decimal_places=0,max_digits=12)
    picture = models.ImageField(upload_to='uploed/products/',blank=True)
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class order(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='',blank=False,max_length=500)
    phone = models.CharField(blank=True,max_length=15)
    data=models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name

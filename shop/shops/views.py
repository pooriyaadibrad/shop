from django.shortcuts import render
from . import models

# Create your views here.
def index(request):


    alldata=models.product.objects.all()
    return render(request=request,template_name='index.html', context={'products':alldata})
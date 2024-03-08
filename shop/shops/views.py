from django.shortcuts import render,redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    alldata=models.product.objects.all()
    return render(request=request,template_name='index.html', context={'products':alldata})
def test(request):
    return render(request=request,template_name='navbar.html')

def loginUser(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request=request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'با موفقیت وارد شدید')
            return redirect('index')
        else:
            messages.error(request,'در ورود مشکلی پیش آمده')
            return render(request=request, template_name='loginForm.html')
    else:
        return render(request=request,template_name='loginForm.html')
def logoutUser(request):
    logout(request)
    messages.success(request,"با موفقیت خارج شدید")
    return redirect('index')
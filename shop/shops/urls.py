
from django.urls import path

from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout')
]
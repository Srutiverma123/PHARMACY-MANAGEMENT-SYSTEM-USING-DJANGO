from django.urls import path,include
from . import views  #importing views.py
                     # . means importing from current folder pharmacy

#list of urls
urlpatterns=[
path('',views.index,name='index'), #home page
path('name',views.name,name='name'),
path('outOfStock',views.outOfStock,name='outOfStock'),
path('expiry',views.expiry,name='expiry'),
path('quantity',views.quantity,name='quantity'),
path('price',views.price,name='price'),]

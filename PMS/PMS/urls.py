from django.contrib import admin  #importing admin.py
from django.urls import path,include
from django.conf import settings  #importing settings.py
from django.conf.urls.static import static #this will help in storing all images eventhough they maybe deleted by admin
from pharmacy import views #importing views.py

urlpatterns = [
path('',include('pharmacy.urls')),
path('admin/', admin.site.urls), #present by default
path('index',views.index,name='index'),
path('name',views.name,name='name'),
path('outOfStock',views.outOfStock,name='outOfStock'),
path('expiry',views.expiry,name='expiry'),
path('quantity',views.quantity,name='quantity'),
path('price',views.price,name='price'),]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #adding all pictures of medicnes
                                                                                     # to media folder


#functions to fetch medicine details

from django.shortcuts import render #render helps to display details to the html files
from .models import Medicine #importing Medicine from models.py
from django.utils import timezone as tz

def index(request):#home page
    med = Medicine.objects.all() #Medicine.objects.all()  -   all medicine rows of table are fetched
    return render(request, 'index.html', {'med': med}) #med is sent to index.html & index.html is dislayed

def name(request):#filter by medicine name
    name=request.GET['name']
    med = Medicine.objects.all()
    return render(request, 'name.html', {'med': med ,'name':name}) #med & name is sent to name.html & name.html
                                                                   # is dislayed

def quantity(request):#filter by medicine quantity
    quan = request.GET['quantity']
    med = []
    for d in Medicine.objects.all():
        if d.quantity >= int(quan) :
         med.append(d)
    return render(request, 'quantity.html', {'med': med}) #med is sent to quantity.html & quantity.html is dislayed

def price(request):#filter by medicine price
    pri=request.GET['price']
    med = []
    for d in Medicine.objects.all():
        if d.price >= int(pri):
            med.append(d)
    return render(request, 'quantity.html', {'med': med}) #med is sent to quantity.html & quantity.html is dislayed

def outOfStock(request):#shows out of stock medicine details
    med = []
    for d in Medicine.objects.all():
        if d.quantity==0:
            med.append(d)
    return render(request, 'quantity.html', {'med': med}) #med is sent to quantity.html & quantity.html is dislayed

def expiry(request):#shows expired medicine details
    today = tz.localtime(tz.now()).date()
    med = []
    for d in Medicine.objects.all():
        if d.exp < today :
         med.append(d)
    return render(request, 'quantity.html', {'med': med}) #med is sent to quantity.html & quantity.html is dislayed

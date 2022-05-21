from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, "services/index.html")
# @login_required(login_url='/login')  
def booking(request):
    if request.method == "POST":
        date=request.POST["date"]
        no=request.POST["tableno"]
        try:
            if(tablebooking.objects.get(date=date)):
                try:
                    if(tablebooking.objects.get(tableno=no)):
                        return render (request,"services/table.html",{"text":"Table Already Booked","dict1":createtable.objects.all()}) 
                except:
                    table=tablebooking.objects.create(tableno=no)
                    table.person2=request.POST["name"]
                    table.date=date
                    table.time=request.POST["time"]
        except:
            table=tablebooking.objects.create(tableno=no)
            table.person2=request.POST["name"]
            table.date=date
            table.time=request.POST["time"]
        table.save()
        return render(request,"services/table.html",{"text":"Table Booked","dict1":createtable.objects.all()})
    else:
        return render (request,"services/table.html",{"dict1":createtable.objects.all()})
def menu(request):
    if request.method == "POST":
        no=request.POST["itemname"]
        table=item.objects.get(itemname=no)
        # list=cart.objects.create(sitem=no)
        # list.squantity=request.POST["quantity"]
        # list.sprice=table.price
        # list.save()
        return render(request,"services/menu.html",{"text":table,"list":item.objects.all()})
    else:
        return render(request,"services/menu.html",{"list":item.objects.all()})
    
def contact(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        subject=request.POST["subject"]
        text=request.POST["text"]
        
        #Send email
        send_mail(
            subject, # subject
            text, # message
            email, # From email
            ["kiran.rokkam456@gmail.com"], # to email
            
        )

        return render(request,'services/contact.html', {'name':name} )
    else: 
        return render(request,'services/contact.html',{})
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
        current=request.user
        no=request.POST["tableno"]
        table=tablebooking.objects.get(tableno=no)
        table.person2=request.POST["name"]
        table.date=request.POST["date"]
        table.time=request.POST["time"]
        table.save()
        
        return HttpResponse("Table Booked")
    else:
        return render (request,"services/table.html",{"dict":tablebooking.objects.all()})
def menu(request):
    if request.method == "POST":
        current=request.user
        no=request.POST["item"]
        table=items.objects.get(item=no)
        list=cart.objects.create(sitem=no)
        list.squantity=request.POST["quantity"]
        list.sprice=(table.price)
        list.save()
        return HttpResponse("Added to cart")
    else:
        return render(request,"services/menu.html",{"list":items.objects.all()})
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
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


# Create your views here.
def index(request):
    return render(request, "services/index.html")
# @login_required(login_url='/login')  
def booking(request):
    if request.method == "POST":
        current=request.user
        table=tablebooking()
        table.person=request.POST["name"]
        table.tableno=request.POST["table no"]
        table.date=request.post["day"]
        table.time=request.post["hour"]
        table.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render (request,"services/table.html",{"dict":costumer.objects.first()})
def menu(request):
    return render(request,"services/menu.html",{"l":costumer.objects.first(),"m":costumer.objects.last()})

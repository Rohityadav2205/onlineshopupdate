from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("this is my online shop")

def user(request):
    return render(request,"mshop.html")
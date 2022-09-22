from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import MshopModel

#
# def mshop(request):
#     mobilename = 0
#     mobileram = 0
#     mobilerom =0
#     mobilecolour = 0
#     mobilebattery = 0
#     price = 0
#     if request.GET:
#         mobilename = request.GET["mobilename"]
#         mobileram =int( request.GET["mobileram"])
#         mobilerom =int (request.GET["mobilerom"])
#         mobilecolour = request.GET["mobilecolour"]
#         mobilebattery =int (request.GET["mobilebattery"])
#         price = int(request.GET["price"])
#
#         ms = MshopModel()
#         ms.mobilename = mobilename
#         ms.mobileram = mobileram
#         ms.mobilerom = mobilerom
#         ms.mobilecolour = mobilecolour
#         ms.mobilebattery = mobilebattery
#         ms.price = price
#         return HttpResponse("App Home")
#
#         ms.save()
#
#         return render(request, "mshop.html", {"mobilename": mobilename, "mobileram": mobileram, "mobilerom": mobilerom,
#                                               "mobilecolour": mobilecolour, "mobilebattery": mobilebattery,
#                                               "price": price})
#
#     return HttpResponse("App Home")
#
#     ms.save()
#     return render(request, "mshop.html", )
#
def mshop(request):
    ms = MshopModel()
    ms.mobilename = "iphone-14"
    ms.mobileram = "6"
    ms.mobilerom = "128"
    ms.mobilecolour = "brownpista"
    ms.mobilebattery = "5000mah"
    ms.price = "97676"

    ms.save()
    return render(request, "mshop.html", )


def add(request):
    a = 0
    b = 0
    total = 0
    if request.GET:
        a = int(request.GET["n1"])
        b = int(request.GET["n2"])
        opt = request.GET["option"]
        ms = MshopModel()
        ms.mobilename = "iphone-14"
        ms.mobileram = a
        ms.mobilerom = b
        ms.mobilecolour = "brownpista"
        ms.mobilebattery = "5000mah"
        ms.price = "97676"

        ms.save()
        print(opt)
        if opt == "add":
            total=a+b

    return render(request, "add.html",{"n1":a,"n2":b,"result":total})

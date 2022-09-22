from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.index),
    path("mshop/", views.mshop),
    path("add/", views.add),
]

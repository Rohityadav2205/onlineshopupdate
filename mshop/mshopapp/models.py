from django.db import models

# Create your models here.
class MshopModel(models.Model):
    mobilename=models.CharField(max_length=220)
    mobileram=models. CharField(max_length=220)
    mobilerom=models. CharField(max_length=100)
    mobilecolour=models.CharField(max_length=100)
    mobilebattery=models.CharField(max_length=200)


    price=models.IntegerField()

def __str__(self):
    return "Mobile Name={0},mobile ram={1},mobile rom={2},mobile colour={3},mobile battery={4},price ={5}".format(self.mobilename,self.mobileram,self.mobilerom,self.mobilecolour,self.mobilebattery,self)
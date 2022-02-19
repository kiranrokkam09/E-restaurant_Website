from django.db import models

# Create your models here.
    
class tablebooking(models.Model):
    person2=models.CharField(max_length=10,blank=True,default='admin')
    tableno=models.IntegerField(max_length=1)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    
    def __str__(self):
     return f"{self.person2} {self.tableno}"
    
class items(models.Model):
    item=models.CharField(max_length=64)
    price=models.IntegerField(max_length=4)
    
    def __str__(self):
     return f"{self.item} {self.price}"
class cart(models.Model):
    sitem=models.CharField(max_length=64)
    sprice=models.IntegerField(max_length=4,null=True)
    squantity=models.IntegerField(max_length=10,null=True)
    
    def __str__(self):
     return f"{self.sitem} {self.sprice}"
# class parking(models.Model):
#     parkingno=models.IntegerField(length=2)
# class billing(models.Model):
#     total=models.IntegerField(length=4)
    
    

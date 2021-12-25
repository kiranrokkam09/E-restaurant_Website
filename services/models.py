from django.db import models

# Create your models here.
class costumer(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    phoneno=models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first} {self.last}"
    
class tablebooking(models.Model):
    # person=models.ForeignKey(costumer,on_delete=models.CASCADE, related_name="tablesbooked")
    person=models.CharField(max_length=10)
    tableno=models.IntegerField(max_length=1)
    date=models.CharField(max_length=10)
    time=models.CharField(max_length=10)
    
    def __str__(self):
     return f"{self.person} {self.tableno}"
    
class menu(models.Model):
    item=models.CharField(max_length=64)
    price=models.IntegerField(max_length=4)
    
    def __str__(self):
     return f"{self.item} {self.price}"
# class parking(models.Model):
#     parkingno=models.IntegerField(length=2)
# class billing(models.Model):
#     total=models.IntegerField(length=4)
    
    

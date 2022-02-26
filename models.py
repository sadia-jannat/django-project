from django.db import models

from datetime import datetime


# Create your models here.
class Food(models.Model):
    myfood = models.CharField(max_length=50)
    myfood_2 = models.CharField(max_length=50)


class Habit(models.Model):
    habit=models.ForeignKey(Food,on_delete=models.CASCADE)

# comfortareena table, create, home and see
#table class name Employee
class Employee(models.Model):

    eid=models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail= models.EmailField()
    econtact = models.CharField(max_length=30)
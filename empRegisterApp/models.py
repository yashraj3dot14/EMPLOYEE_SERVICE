from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    empcode = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position, on_delete=models.CASCADE) #on_delete: when we delete any record from parent table, it wil automatically delete this record from this sub table

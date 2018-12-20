from django.db import models

# Create your models here.class

class Store_Data(models.Model):
    name1=models.CharField(max_length=1000)
    db1=models.DateField(null=False,blank=False)
    name2=models.CharField(max_length=1000)
    db2=models.DateField(null=False,blank=False)
    result=models.IntegerField()


    def __str__(self):
        return self.name1+self.name2



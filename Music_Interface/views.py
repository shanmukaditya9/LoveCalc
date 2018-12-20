from django.shortcuts import render
from .models import Store_Data
from django.contrib import messages
import functools
import random

# Create your views here.

def home(request):
    return render(request,'Music_Interface/home.html')

def lovecalc(request):
    if request.method=='POST':
        name1=request.POST['name1']
        if not name1:
            messages.warning(request,'Please enter the name')
        print(name1)
        db1=request.POST['db1']
        name2 = request.POST['name2']
        db2 = request.POST['db2']
        n1=name1
        n2=name2
        s1 = n1.replace(' ', '')
        s2 = n2.replace(' ', '')
        op1 = str(Elab(s1.upper()))
        op2 = str(Elab(s2.upper()))
        rslt=op1+op2
        if (len(rslt) >= 10):
            result = random.randrange(95, 101)
        elif (len(rslt) == 9):
            result = random.randrange(91, 100)
        elif (len(rslt) == 8):
            result = random.randrange(85, 90)
        elif (len(rslt) == 7):
            result = random.randrange(75, 85)
        elif (len(rslt) == 6):
            result = random.randrange(55, 75)
        elif (len(rslt) == 5):
            result = random.randrange(45, 55)
        elif (len(rslt) == 4):
            result = random.randrange(35, 45)
        elif (len(rslt) == 3):
            result = random.randrange(20, 35)
        elif (len(rslt) == 2):
            result = random.randrange(10, 20)
        else:
            result = random.randrange(1, 10)
        ds = Store_Data(name1=name1, db1=db1, name2=name2, db2=db2,result=result)
        print(ds)
        ds.save()
        return render(request,'Music_Interface/home.html',{'n1':n1,'n2':n2,'result':result})
    return render(request,'Music_Interface/home.html')


def Elab(name):
    s={}
    for i in range(65,91):
        s[chr(i)]=i
    b=[]
    for i in name:
        b.append(s.get(i,[0]))
    num1=functools.reduce(lambda x,y:x+y,b)
    return num1



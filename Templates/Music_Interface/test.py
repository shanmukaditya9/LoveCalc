import functools
import random
def Elab(name):
    s={}
    for i in range(65,91):
        s[chr(i)]=i
    b=[]
    for i in name:
        b.append(s.get(i,[0]))
    num1=functools.reduce(lambda x,y:x+y,b)
    return num1


e1=input('Enter First Name:')
e2=input('Enter Second Name:')
s1=e1.replace(' ','')
s2=e2.replace(' ','')
op1=str(Elab(s1.upper()))
op2=str(Elab(s2.upper()))
rslt=op1+op2
if (len(rslt)>=10):
    result=random.randrange(95,101)
elif (len(rslt)==9):
    result = random.randrange(91, 100)
elif (len(rslt)==8):
    result = random.randrange(85, 90)
elif (len(rslt)==7):
    result = random.randrange(75, 85)
elif (len(rslt)==6):
    result = random.randrange(55, 75)
elif (len(rslt)==5):
    result = random.randrange(45, 55)
elif (len(rslt)==4):
    result = random.randrange(35, 45)
elif (len(rslt)==3):
    result = random.randrange(20, 35)
elif (len(rslt)==2):
    result = random.randrange(10, 20)
else:
    result=random.randrange(1,10)
print(result)
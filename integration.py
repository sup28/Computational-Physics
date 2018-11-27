import random

def fun(x):
    y=0.2 + 25*x-200*x*x+675*x**3-900*x**4+400*x**5
    return y

a=0.0
b=.8
h=.01

def trap(a,b):
    area=(fun(a)+fun(b))*(b-a)/2
    return area

area=0.0
def multitrap(a,b):
    area=0.0
    for i in range(0,int((b-a)/h)):
        area+=trap(a+i*h,a+(i+1)*h)
    return area
    
    
n=100
x=[]
x.append(1.0)
def modulo():
    k=4
    c=5
    M=97
    sum=0.0
    for i in range(1,n):
        x.append((k*x[i-1]+c)%M)
        sum+=fun(((x[i]/97))*(.8))
        #print fun(x[i])
    sum/=(n-1)
    return sum
        
def randomnum():
    x=[]
    sum=0.0
    for i in range(0,n):
        x.append((random.randint(0,97)/97.0)*.8)
        sum+=fun(x[i])
        #print(x[i])
    area=(sum/(n-1))*.8
    return area
        
        

print "Multi trap is:",multitrap(a,b)
print "Trapezium is :",trap(a,b)
print "Modulo random number is :",modulo()*(b-a)
print "Random number is :",randomnum()

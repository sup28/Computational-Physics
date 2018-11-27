# -*- coding: utf-8 -*-



import math
import numpy as np
n=5  #int(raw_input())
a=np.diag(np.zeros(n,dtype=np.float128))#making a 10 D array to accumulate higher order states
for j in range(4):
    a[j][j+1]=math.sqrt(j+1)
#a=np.array([[0,math.sqrt(1),0,0,0],[0,0,math.sqrt(2),0,0],[0,0,0,math.sqrt(3),0],[0,0,0,0,math.sqrt(4)],[0,0,0,0,0]],dtype=np.float128)
b=np.transpose(a)
x=(a+b)/math.sqrt(2.0)
#print x
x=(np.dot(np.dot(x,x),np.dot(x,x)))
#x=np.dot(x,x)
#print x
H=np.diag(np.zeros(n,dtype=np.float128))
for j in range(n):
    H[j][j]=(2*j+1)/2.0
for l in range(11):
    H1=H+(l/10.0)*x
    #print H1
    theta=float(0.0)
    tan=float(0.0)
    sin=float(0.0)
    cos=float(0.0)
    R=np.diag(np.ones(n,dtype=np.float128))
    #rotation=np.diag([0,0,0])
    for m in range(100):
        for i in range(5):
            for j in range(i,5):
                if(i!=j):                
                    if(H1[i][j]>0.0001):
                        theta=(H1[j][j]-H1[i][i])/(H1[i][j]*2)
                        #print H1
                        if(theta!=0):
                            tan=(math.fabs(theta)/theta)/(math.fabs(theta)+math.sqrt(theta*theta+1))
                            #print theta, tan
                            cos=1/math.sqrt(1+tan*tan)
                            sin=cos*tan
                    #           D=H1`````````````````````````````````````````````
                    #           D[i][j]=0
                    #           D[j][i]=0
                    #           D[i][i]=c````````````````````````````````os*cos*H1[i][i]+sin*sin*H1[j][j]-2*cos*sin*H1[i][j]
                    #           D[j][j]=sin*sin*H1[i][i]+cos*cos*H1[j][j]+2*cos*sin*H1[i][j]
                            R=np.diag(np.ones(n,dtype=np.float128))                 
                            R[i][i]=cos
                            R[j][j]=cos
                            R[i][j]=sin
                            R[j][i]=-sin
                            #print R
                            H1=np.dot(np.transpose(R),np.dot(H1,R))
                            #print H1
    print (l/10.0),
    v=np.diag(H1)
    for j in range(5):
        print v[j],
    print ("\n")
 #GNU plot:   "Documents/Computational Physics/123.txt"u 1:2 w lp

   

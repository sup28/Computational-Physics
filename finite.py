# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:44:19 2017

@author: harsh
"""
h1=.01
Ta=20.0
import numpy as np
def ydoublediff(T):
    return (-h1*(Ta-T))

len=10.0
step=int(raw_input())
h=len/step
A=np.zeros((step-1,step-1))
T=np.zeros(step-1)
y=np.ones(step-1)*Ta*h*h*h1
T0=40.0
T10=200.0
y[0]=T0+Ta*h*h*h1
y[-1]=T10+Ta*h*h*h1
for i in range(step-2):
    A[i][i]=2+h1*h*h
    A[i][i+1]=-1
    A[i+1][i]=-1

A[step-2][step-2]=2+h1*h*h

for i in range(step-2):
    k=A[i][i+1]/A[i][i]
    y[i+1]-=k*y[i]
    for j in range(i,step-1):
        A[i+1][j]-=k*A[i][j]

T[-1]=y[-1]/A[-1][-1]

for i in range(step-3,-1,-1):
    T[i]=(y[i]-T[i+1]*A[i][i+1])/A[i][i]
    

print T0
print T
print T10


# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:18:41 2017

@author: harsh
"""

import numpy as np
h1=.01
Ta=20.0
steps=20#int(raw_input())
def ky(z):
    return z
def kz(y):
    return  (h1*(y-Ta))

h=10.0/steps
T0=40.0
T10=200.0
y=np.zeros(steps+1)
z=np.zeros(steps+1)
x=[h*i for i in range(steps+1)]
y[0]=T0
z1=10.0         #assuming
z[0]=z1
for i in range(steps):
    k1y,k1z=ky(z[i]),kz(y[i])
    k2y,k2z=ky(z[i]+k1z*h/2),kz(y[i]+k1y*h/2)
    k3y,k3z=ky(z[i]+k2z*h/2),kz(y[i]+k2y*h/2)
    k4y,k4z=ky(z[i]+k3z*h),kz(y[i]+k3y*h)
    y[i+1]=y[i]+(k1y+2*k2y+2*k3y+k4y)*h/6
    z[i+1]=z[i]+(k1z+2*k2z+2*k3z+k4z)*h/6

y1=y[-1]


z2=20.0
z[0]=z2
for i in range(steps):
    k1y,k1z=ky(z[i]),kz(y[i])
    k2y,k2z=ky(z[i]+k1z*h/2),kz(y[i]+k1y*h/2)
    k3y,k3z=ky(z[i]+k2z*h/2),kz(y[i]+k2y*h/2)
    k4y,k4z=ky(z[i]+k3z*h),kz(y[i]+k3y*h)
    y[i+1]=y[i]+(k1y+2*k2y+2*k3y+k4y)*h/6
    z[i+1]=z[i]+(k1z+2*k2z+2*k3z+k4z)*h/6

y2=y[-1]

z3=z1+(200-y1)*(z1-z2)/(y1-y2)
z[0]=z3
for i in range(steps):
    k1y,k1z=ky(z[i]),kz(y[i])
    k2y,k2z=ky(z[i]+k1z*h/2),kz(y[i]+k1y*h/2)
    k3y,k3z=ky(z[i]+k2z*h/2),kz(y[i]+k2y*h/2)
    k4y,k4z=ky(z[i]+k3z*h),kz(y[i]+k3y*h)
    y[i+1]=y[i]+(k1y+2*k2y+2*k3y+k4y)*h/6
    z[i+1]=z[i]+(k1z+2*k2z+2*k3z+k4z)*h/6
    
#print T0
print y
print T10

print z[0]


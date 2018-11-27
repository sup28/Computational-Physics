
h = float(input())
n1 = 4/h
n=int(n1+1)

ansactual = []
for  i in range(0,n):
    x = i*h	
    y = -0.5*(x)**4 + 4*(x)**3 - 10*(x)**2 + 8.5*(x) + 1
    ansactual.append(y)
    
anseuler = [1]
for i in range(1,n):
    x = (i-1)*h
    y1 = anseuler[i-1] + (-2*x**3+12*x**2-20*x+8.5)*h
    anseuler.append(y1)
    
ansheun = [1]
for i in range(1,n):
    x = i*h
    x1 = (i-1)*h
    s1 = - 2*(x)**3+12*(x)**2-20*(x)+8.5
    s2 = -2*(x1)**3+12*(x1)**2-20*(x1)+8.5
    s = (s1+s2)/2
    y2 = ansheun[i-1] + s*h
    ansheun.append(y2)

errorheun = []
for i in range(0,n):
    z = (ansheun[i]-ansactual[i])*100/ansactual[i]
    errorheun.append(z)

erroreuler = []
for i in range(0,n):
    z1 = (anseuler[i]-ansactual[i])*100/ansactual[i]
    erroreuler.append(z1)

##print("X\t\tY(exact)\tY(heun)\t%error(heun)\tY(euler)\t%error(euler")
##print("\n")
##for i in range(0,9):
 ##   x = i/2
  ##  print(x,"\t\t",ansactual[i],"\t",ansheun[i],"\t\t",errorheun[i],"\t",anseuler[i],"\t\t",erroreuler[i])
  ##  print("\n")
    
    
    
print("value_x\tvalue_actual\tvalue_heun\theun_error\tvalue_euler\teuler_error")
for i in range(0,n):
   x = i*h
   print("%.6lf\t%.6lf\t%.6lf\t%.6lf\t%.6lf\t%.6lf" %(float(x),ansactual[i],ansheun[i],errorheun[i],anseuler[i],erroreuler[i])) 	
    
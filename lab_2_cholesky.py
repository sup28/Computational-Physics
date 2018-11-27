#Lab No:2
# Title : Cholesky Decomposition Method
# Date: 17/08/2017



import math

print('No.of variables:')
n = int(input())
print('Elements of the Coefficient Matrix:')
a = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j]=float(input())

l = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(0,i+1):
        sum=0
        for k in range(j):
             sum=sum+l[i][k]*l[j][k]
        if i==j:
            l[i][i]=math.sqrt(a[i][i]-sum)
        else:
            l[i][j]=(a[i][j]-sum)/l[j][j]

l_transpose = [[0 for j in range(n)] for i in range(n)]
for x in range(n):
    for y in range(n):
        l_transpose[x][y]=l[y][x]

print("L:")
print(l)

print("L TRANSPOSE:")
print(l_transpose)

mult = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
      for j in range(n):
              for k in range(n):
                   mult[i][j] += l[i][k] * l_transpose[k][j]

print("L*L-Transpose:")
print(mult)

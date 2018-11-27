#Lab No:2
# Title : LU decomposition
# Date: 17/08/2017


print('No.of variables:')
n = int(input())
print('Elements of the Coefficient Matrix:')
a = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j]=float(input())
u=a

l = [[0 for j in range(n)] for i in range(n)]
for z in range(0,n):
    for x in range(z+1,n):
        ratio= float(u[x][z])/u[z][z]
        l[x][z]=ratio
        for y in range(0,n):
                u[x][y]= u[x][y]-ratio*u[z][y]

for k in range(n):
    l[k][k]=1

print('U is:')
print(u)
print('L is:')
print(l)



print('Enter the constant matrix:')
c=[0 for x in range(n)]
for x in range(n):
    c[x]=float(input())

y=[0 for x in range(n)]
for i in range(n):
    sum=0
    for x in range(0,i):
        sum=sum+l[i][x]*y[x]
    y[i]=(c[i]-sum)/l[i][i]


sol=[0 for x in range(n)]
for i in range(n-1,-1,-1):
    sum=0
    for x in range(i,n):
        sum=sum+u[i][x]*sol[x]
    sol[i]=(y[i]-sum)/u[i][i]
print("Solution is:")
print(sol)


I = [[0 for j in range(n)] for i in range(n)]
for x in range(n):
    I[x][x]=1

sol = [[0 for j in range(n)] for i in range(n)]

for k in range(n):
    y=[0 for x in range(n)]
    for i in range(n):
        sum=0
        for x in range(0,i):
            sum=sum+l[i][x]*y[x]
        y[i]=(I[k][i]-sum)/l[i][i]




    for i in range(n-1,-1,-1):
        sum=0
        for x in range(i,n):
            sum=sum+u[i][x]*sol[k][x]
        sol[k][i]=(y[i]-sum)/u[i][i]


sol_transpose = [[0 for j in range(n)] for i in range(n)]
for x in range(n):
    for y in range(n):
        sol_transpose[x][y]=sol[y][x]



print("Inverse is:")
print(sol_transpose)

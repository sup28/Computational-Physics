#Lab No:1
# Title : Guass Elimination



def pivot(a,n):
    for z in range(0,n):
        for x in range(z+1,n):

            if abs(a[x][z]) > abs(a[z][z]):
                #Ascending order
                a[x],a[z]=a[z],a[x]

            ratio= float(a[x][z]/a[z][z])
            print (ratio)
            for y in range(0,n+1):
                a[x][y]= a[x][y]-ratio*a[z][y]
    return a

def for_elem (a,n):
    #Upper-Triangular
    for z in range(0,n):
        for x in range(z+1,n):
            ratio= float(a[x][z])/a[z][z]
            for y in range(0,n+1):
                a[x][y]= a[x][y]-ratio*a[z][y]
    return(a)

def back_subs(a,n):
    sol=[0 for x in range(n)]
    for z in range(n-1,-1,-1):
        sum=0
        for y in range(z+1,n):
            sum=sum+a[z][y]*sol[y]
        sol[z]=(a[z][n]-sum)/a[z][z]
    return sol

def Gauss_Jor(a,n):
    #diagonalization
    for z in range(0,n):
        for x in range(0,n):
            if x!=z:
                ratio= float(a[x][z])/a[z][z]
                for y in range(0,n+1):
                    a[x][y]= a[x][y]-ratio*a[z][y]

    for s in range(n):
        div=a[s][s]
        a[s]=[x/div for x in a[s]]
    #Identity matrix creation

    sol=[0 for t in range(n)]
    for x in range(n):
        sol[x]=a[x][n]
    return(sol)


print('No.of variables:')
n = int(input())
print('Elements of the Matrix:')
b = [[0 for j in range(n+1)] for i in range(n)]

for i in range(n):
    for j in range(n+1):
        b[i][j]=float(input())
        
a=b


print('Choose a method:')
print('1 for Gauss-Jordan')
print('2 for Pivot Gauss-Elimination')
print('3 for Non- Pivot  Gauss-Elimination')

m=int(input())

if m==1:
    answer=Gauss_Jor(a,n)
elif m==2:
    inter=pivot(a,n)
    answer=back_subs(inter,n)
else:
    inter=for_elem(a,n)
    answer=back_subs(inter,n)

print("Answer:")
print(answer)

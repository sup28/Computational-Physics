import numpy as np
import sys

filename=sys.argv[1]
n=raw_input()
l=0.6
n=int(n)
#print("Input matrix is  ")
#A = np.reshape(A, (-1, 2))
#infile=pd.read_csv(filename)
#A=infile.reset_index().values
#A=infile.as_matrix()
#print(A)
#print(A.shape)

A=np.array([[input() for j in range(n)] for i in range(n)],dtype=np.float32)
#A.astype(float)
B=np.linalg.inv(A)

x=np.array([input() for i in range(n)],dtype=np.float32)
#x.astype(float)
print ("Inverse Matrix is :")
print B
mul=np.array([j for j in range(n)],dtype=np.float32)

I=(.000001)*np.array([1 for j in range(n)],dtype=np.float32)    
while np.any((I)<=(abs(mul-x))):
    x=mul
    mul=np.matmul(A,np.transpose(x))
    print mul
    big=np.float(np.amax((mul[np.nonzero(mul)])))
    print big
    #big.astype(float)
    mul=mul/(np.float(big))
    print(mul)
    

l1=np.amax(np.matmul(A,np.transpose(x))/x)
mul=np.array([j for j in range(n)],dtype=np.float32)
while np.any((I)<=(abs(mul-x))):
    x=mul
    mul=np.matmul(B,np.transpose(x))
    print mul
    big=np.float(np.amax((mul[np.nonzero(mul)])))
    print big
    #big.astype(float)
    mul=mul/(np.float(big))
    print(mul)
l2= 1/(np.amax(np.abs((np.matmul(B,np.transpose(x))/x))))
print("Largest Eigen Value is :"),
print l1
print("Smallest Eigen Value is :"),
print l2
#Largest EigenValue

 
 
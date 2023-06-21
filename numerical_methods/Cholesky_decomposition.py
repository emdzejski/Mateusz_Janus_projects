import numpy as np
from math import sqrt
from Zad_3_1 import LU 

C = np.array([[3,2,0,0],[2,3,2,0],[0,2,3,2],[0,0,2,3]])
D = np.array([[3.0e-10,1,0,0], [1,3.0e-10,1,0], [0,1,3.0e-10,1],[0,0,1,3.0e-10]])
def cholesky(a):
    n,m = a.shape
    c = np.zeros((n,m))
    for i in range(n):
            for k in range(i+1):
                tmp_sum = sum(c[i,j] * c[k,j] for j in range(k))
                
                if (i == k): 
                    c[i,k] = sqrt(a[i,i] - tmp_sum)
                else:
                    c[i,k] = (1/ c[k,k] * (a[i,k] - tmp_sum))
    return c 

L,U = LU(C)
print(L)
print()
print(U)
print()
lower, upper = LU(D)
print(lower)
print()
print(upper)
#cholesky(C) -- skrypt kończy się błędęm, bo macierz nie jest dodatnio okreslona
#cholesky(D) -- analogiczna sytuacja 
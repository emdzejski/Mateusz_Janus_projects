#wybrałem faktoryzację qr, ponieważ umożliwia ona rozwiązanie układu z macierzą 3-diagonalną
#w czasie liniowym
from math import sqrt
import numpy as np
a = np.array([[3,1,0,0,0,0,0],[1,4,1,0,0,0,0],[0,1,4,1,0,0,0],[0,0,1,4,1,0,0],[0,0,0,1,4,1,0],[0,0,0,0,1,4,1],[0,0,0,0,0,1,3]])
d = np.array([1,2,3,4,5,6,7])
n,m = np.shape(a)
def g_maker(i,j,a): #funckja tworzy macierz givensa
    g = np.identity(7)
    #cosinusy
    g[i][i] = a[j][j]/sqrt(a[j][j]**2 + a[i][j]**2)
    g[j][j] = a[j][j]/sqrt(a[j][j]**2 + a[i][j]**2)
    #sinusy
    g[j][i] = a[i][j]/sqrt(a[j][j]**2 + a[i][j]**2)
    g[i][j] = -a[i][j]/sqrt(a[j][j]**2 + a[i][j]**2)
    return g
    
def qr(a,d): #przy pomocy givensów robię faktoryzację
    for i in range(n-1):
        g = g_maker(i+1,i,a)
        a_n = np.dot(g,a) #tutaj oczywiście przydałby się algorytm mnożenia pomijający 0 i 1
        a = a_n
        if abs(a[i+1][i]) < 1e-15:
            a[i+1][i] = 0
        d_n = np.dot(g,d) 
        
        d = d_n
        
    return a,d
b,c = qr(a,d)


def backsubs(b,c): #backsubstitution
    x = [1]*n
    x[-1]= (c[-1]/b[-1][-1])
    x[-2] = (c[-2] - b[-2][-1]*x[-1])/b[-2][-2]
    for k in range(4,-1,-1):
        x[k] = (c[k] - b[k][k+2]*x[k+2] - b[k][k+1]*x[k+1])/a[k][k]
    return x 
x_1 =backsubs(b,c)

#tworzę 2. macierz
e = np.zeros((7,7))
for i in range(7):
    e[i][i] = 4
for i in range(6):
    e[i+1][i] = 1
for i in range(6):
    e[i][i+1] = 1
e[6][0] = 1
e[0][6] = 1
# używam algorytmu Shermana-Morrisona, ponieważ rozwiązanie ukłądu z drugą macierzą było łatwiejsze z powodu 
# znajomości faktoryzacji qr pierwszej macierzy 
u = np.array([1,0,0,0,0,0,1])
e,u_1 = qr(a,u)
q = backsubs(e,u_1)
factor = (np.dot(np.transpose(u), x_1))/(1 + np.dot(np.transpose(u),q))
fac_x_q = np.multiply(q,factor)
w = np.subtract(np.array(x_1),fac_x_q)
print(w) #---> rozwiązanie 2. układu równań








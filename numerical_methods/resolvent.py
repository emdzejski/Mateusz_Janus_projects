import numpy as np
a = np.array([[2,-1,0,0,1],[-1,2,1,0,0],[0,1,1,1,0],[0,0,1,2,-1],[1,0,0,-1,2]])
tau = 0.38197
rez = a - tau*np.identity(5)
def LU(a):
    n,m = a.shape
    l = np.identity(n)
    u = np.zeros((n,m))
    
    for j in range(n):
        
        for i in range(j+1):
            s1 = sum(u[k][j] * l[i][k] for k in range(i))
            u[i][j] = a[i][j] - s1

                                                                                                                                                                          
        for i in range(j, n):
            s2 = sum(u[k][j] * l[i][k] for k in range(j))
            l[i][j] = (a[i][j] - s2) / u[j][j]
    
    return (l,u)

def forwardsubs(l,b):
    x = [0]*5
    for i in range(5):
        x[i] = (b[i] - sum(l[i][j]*x[j] for j in range(i-1)))/l[i][i]
    return np.array(x)

def backsubs(u,b):
    x = [0]*5
    for i in range(4,-1,-1):
        x[i] = (b[i] - sum(u[i][j]*x[j] for j in range(1,5)))/u[i][i]
    return np.array(x)


y = np.array([1]+[0]*4)
l,u = LU(rez)
for i in range(50):
    w = forwardsubs(l,y)
    z = backsubs(u,w)
    y = z/np.linalg.norm(z)
  
print("szukany wektor to:")
print(y)
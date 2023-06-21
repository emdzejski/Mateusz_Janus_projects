import numpy as np
arr = np.array([[1,2,2,3],[-2,1,0,-1],[1,0,1,2],[-2,0,1,0]])
arr_2 = np.array([[2,5,7],[2,2,8],[2,9,10]])
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
    

if __name__ == '__main__':
    a, b = LU(arr)
    print(a)
    print()
    print(b)
    print()
    c,d = LU(arr_2)
    print(c)
    print()
    print(d)
    


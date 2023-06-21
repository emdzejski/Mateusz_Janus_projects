from numpy import array, zeros, fabs, linalg, identity
#podpunkt a)
A = array([[3,0,3],[2,1,2],[1,2,0]],float)
X = array(['x','y','z'])
B = array([3,1,4],float)
eigvals = linalg.eigvals(A)
eigen_max = max([abs(x) for x in eigvals])
eigen_min = min([abs(x) for x in eigvals])
wspl_uwar = eigen_max/eigen_min
print(f"Współczynnik uwarunkowania macierzy {A} wynosi {wspl_uwar}")

#podpunkt b)
def gauss(a,b):
    n = len(b) 
    x = zeros(n) 

    
    for k in range(n-1):
        for i in range(k+1,n):
            if a[i,k] == 0:
                continue

            factor = a[k,k]/a[i,k]
            for j in range(k,n):
                a[i,j] = a[k,j] - a[i,j]*factor
                
            b[i] = b[k] - b[i]*factor
    print(a)
    print(b)

    
    x[n-1] = b[n-1] / a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
    
        for j in range(i+1, n):
            sum_ax += a[i,j] * x[j]
            
        x[i] = (b[i] - sum_ax) / a[i,i]

    print("Rozwiązania x, y, z, to kolejno:")
    print(x)
#podpunkt c)
def gauss_pivot(a,b):
    n = len(b) 
    x = zeros(n, float) 

    for k in range(n-1):
        if fabs(a[k,k]) < 0: 
            
            for i in range(k+1,n): 
                if fabs(a[i,k]) > fabs(a[k,k]):
                    a[[k,i]] = a[[i,k]]
                    b[[k,i]] = b[[i,k]]
                    break

        for i in range(k+1,n):
            if a[i,k] == 0:
                continue

            factor = a[k,k]/a[i,k]
            for j in range(k,n):
                a[i,j] = a[k,j] - a[i,j]*factor
                
            b[i] = b[k] - b[i]*factor
    print(a)
    print(b)

    x[n-1] = b[n-1] / a[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_ax = 0
    
        for j in range(i+1, n):
            sum_ax += a[i,j] * x[j]
            
        x[i] = (b[i] - sum_ax) / a[i,i]

    print("Rozwiązania x, y, z, to kolejno: ")
    print(x)





print()
gauss(array([[3,0,2],[0,1,1],[2,1,1]]),array([3,1,4]))
print()
gauss_pivot(array([[3,0,2],[0,1,1],[2,1,1]]),array([3,1,4]))

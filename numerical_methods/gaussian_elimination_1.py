from numpy import array, zeros, fabs

a = array([[1,2,-1],[0,1,1],[2,0,-1]], float) #macierz współczynników
b = array([1,2,3], float) #macierz wyrazów wolnych


n = len(b) #n jako liczba niewiadomych
x = zeros(n, float) #wektor rozwiązań

#iteruję po wierszach
for k in range(n-1):
    if fabs(a[k,k]) == 0: #sprawdzam czy element podstawowy jest równy zero 
        
        for i in range(k+1, n): 
            if fabs(a[i,k]) > fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
                break

 #eliminacja gaussa:

    for i in range(k+1,n):
        if a[i,k] == 0:
            continue

        factor = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*factor
            
        b[i] = b[k] - b[i]*factor
print(a)
print(b)

#rozwiązuje równania i umieszczam je w wektorze x
x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0
  
    for j in range(i+1, n):
        sum_ax += a[i,j] * x[j]
        
    x[i] = (b[i] - sum_ax) / a[i,i]

print("Rozwiązania x, y, z, to kolejno: ")
print(x)

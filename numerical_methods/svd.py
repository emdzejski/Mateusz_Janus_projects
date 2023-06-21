import numpy as np
from math import sqrt
arr = np.array([[1,1],[1,-1]])
arr_2 = np.array([[7/6,-1/3,-5/6],[-1/3,2/3,-1/3],[-5/6,-1/3,7/6]])

    
def svd(a):
    #tworzenie macierzy A^T * A
    n,m = np.shape(a)
    arr_t = np.transpose(a)
    prod = np.dot(arr_t,a)
    #uzyskiwanie wartości i wektorów własnych
    eigvals, eigvecs = np.linalg.eig(prod)
    v = np.zeros((m,m))
    diag = np.eye(n,m)
    u = np.zeros((n,n))
    #sortowanie wartości własnych od najmniejszej do największej i odpowiednie sortowanie wektorów
    idx = eigvals.argsort()[::-1]   
    eigenValues = eigvals[idx]
    eigenVectors = eigvecs[:,idx]
    #lista wartości osobliwych
    sing_vals = [sqrt(x) for x in eigenValues]
    for i in range(n):
        diag[i,i] = sing_vals[i] 
    for i in range(m):
        v[i,:] = eigenVectors[:,i] 
    for i in range(n):
        u[:,i] = np.dot(a,v[i,:])/sing_vals[i]
    print(np.dot(np.dot(u,diag),v))
    print()
    print(u)
    print()
    print(diag)
    print()
    print(v)
    return (u,diag,v)
    
def svd_solve(a,b):
    u,diag,v =  svd(a)
    n,m = np.shape(diag)
    #odwrotność macierzy diagonalnej
    for i in range(n):
        diag[i,i] = 1/diag[i,i]
    new_v = np.transpose(v)
    new_u = np.transpose(u)
    #mnożenia macierzowe, które doprowadzą do wektora rozwiązań
    c = np.dot(new_v,diag)
    d = np.dot(c,new_u)
    sol = np.dot(d,b)
    print(sol) 

svd_solve(arr_2,np.array([-1,0,1]))

#svd(arr_1) 



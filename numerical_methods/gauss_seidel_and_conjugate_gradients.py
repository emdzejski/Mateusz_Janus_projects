
import numpy as np
import matplotlib .pyplot as plt

a = np.array([[3,1,1],[1,3,1],[1,1,3]])
e = np.array([1,1,1])
x = [0,0,0]
def g_s(a,b,x): #metoda Gaussa-Seidela zakomentowane linijki miały służyć do stworzenia danych
    #potrzebnych do wykresu
    n = len(b)
    counter = 0
    #plot = []
    while True:
        x_approx = [0]*n
        for i in range(n):
            x_approx[i] = (b[i] -sum(a[i][j]*x_approx[j] for j in range(i)) - sum(a[i][j]*x[j] for j in range(i+1,n)))/a[i][i]
        
        
        if np.allclose(np.array(x),np.array(x_approx),rtol=1e-8): 
            break
        
        #plot.append(np.linalg.norm(np.array(x)-np.array(x_approx)))

        x = x_approx
        counter +=1
    return x, counter


def cg(a,b,x): #gradienty sprzężone, zakomentowane linijki miały służyć do stworzenia danych
    #potrzebnych do wykresu
    r = b - np.dot(a,x)
    p = r.copy()
    counter = 0
    #plot = []
    while np.linalg.norm(r)>1e-8:
        r_t = np.transpose(r)
        p_t = np.transpose(p)
        Ap = np.dot(a,p)
        alpha = np.dot(r_t,r)/np.dot(p_t,Ap)
        r1 = r - np.multiply(alpha,Ap)
        beta = np.dot(np.transpose(r1),r1)/np.dot(r_t,r)
        p1 = r1 +np.multiply(beta,p)
        x1 = x + np.multiply(alpha,p)
        #plot.append(np.linalg.norm(np.array(x)- np.array(x1))) 
        r = r1
        p = p1
        x = x1
        counter += 1
    return x, counter

#tworzę macierz 128x128
a_1 = np.zeros((128,128))
e_1 = np.array([1]*128)
for i in range(128):
    a_1[i][i] = 4
for i in range(127):
    a_1[i+1][i] = 1
for i in range(127):
    a_1[i][i+1] = 1
for i in range(124):
    a_1[i+4][i] = 1
for i in range(124):
    a_1[i][i+4] = 1

x1 = [0]*128

GS_128x128  = g_s(a_1,e_1,x1)[0] #rozw. układu z macierzą 128x128, metoda Gaussa-Seidela
GS_3x3 = g_s(a,e,x)[0] #rozw. układu z macierzą 3x3, metoda Gaussa-Seidela

GC_3x3  = cg(a,e,x)[0] #rozw. układu z macierzą 3x3, metoda gradientów sprzężonych
GC_128x128 = cg(a_1, e_1,x1)[0] #rozw. układu z macierzą 128x128, metoda gradientów sprzężonych
print('rozwiązania macierzy 3x3 metodą Gaussa-Seidela:')
print(GS_3x3)
print()
print("rozwiązania macierzy 3x3 metodą grandientów sprzężonych:")
print(GC_3x3)
"""
print('rozwiązania macierzy 3x3 metodą Gaussa-Seidela:')
for i in range(len(GS_128x128)):
    print(GS_128x128[i])

print()
print('rozwiązania macierzy 3x3 metodą gradientów sprzężonych:')
for i in range(len(CG_128x128)):
    print(CG_128x128[i])

"""
#zakomentowane, żeby nie było bałaganu przy wyświetlaniu
    

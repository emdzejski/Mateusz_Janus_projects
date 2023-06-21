#a)
""" nie jest to macierz rzadka, gdyż liczba elementów niezerowych będzie równa liczbie elementów zerowych.
(po przestawieniu odpowiednich wyrazów otrzymamy macierz, 
w której mamy na zmianę wiersz (bądź kolumnę) wyrazów niezerowych i zerowych.)"""

#b)
""" macierz możnaby przechowywać jako listę zawierającą listy. Listy wewnętrzne odpowiadałyby odpowiednim
wierszom macierzy."""
""" algorytm zawierałby instrukcję warunkową, która sprawdzałaby parzystość indeksu wierszy. Następnie, 
w zależności od tego, czy indeks jest parzysty czy nie, wykonywałby mnożenie macierzowe pomijając co drugi 
element począwszy od odpowiedniego elementu(indeks 0 lub 1); złożoność obliczeniowa algorytmu
wynosi O(N^2/2)"""

#proof of concept dla macierzy 3x3 i 4x4
def mat_vec_mult(a,x):
    n = len(a)
    b = n * [0]
    for i in range(n):
        if a.index(a[i]) % 2 == 0:
            for j in range(0,n,2):
                b[i] += a[i][j] * x[j]
        else:
            for k in range(1,n,2):
                b[i] += a[i][k] * x[k]
    return b

a = [[1,0,2],[0,3,0],[2,0,4]]
z = [1,2,3]
b =[[1,0,2,0],[0,3,0,4],[2,0,5,0],[0,4,0,6]]
y = [1,2,3,4]

print(mat_vec_mult(b,y))
print(mat_vec_mult(a,z))
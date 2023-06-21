from random import random


from math import sqrt
def pi(n):
    i = 0 #licznik prób
    j = 0 #licznik trafień
    while i < n:
        x = random()
        y = random()
        if sqrt(x**2 + y**2) < 1:
            j += 1 
        i += 1 
    return 4*j/i
for k in range(1,6):
    print(f"przybliżenie pi dla n ={10**k} --- {pi(10**k)} ")
    print()
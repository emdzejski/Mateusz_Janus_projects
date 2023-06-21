from random import random
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
def generator():
    x = random()
    if x > 0 and x <= 1/6:
        y = sqrt(6*x) - 1
    if x > 1/6 and x <= 5/6:
        y = 3*x - 0.5
    if x > 5/6 and x <= 1:
       y =  3 - sqrt(6- 6*x)
    return y
vals = []
vals2 = []
for i in range(1000):
    vals.append(generator())

for i in range(100000):
    vals2.append(generator())


plt.hist(vals,50, density = True)
x1 = np.linspace(-1,0)
y1 = [1/3 * x + 1/3 for x in x1]
plt.plot(x1,y1, color = 'm')
x2 = np.linspace(0,2)
y2 = [1/3]*50
plt.plot(x2,y2, color = 'm')
x3 = np.linspace(2,3)
y3 = [-1/3 * x + 1 for x in x3]
plt.plot(x3,y3, color = 'm')
plt.title('1000 generated points')
plt.show()

plt.close() #po zamknięciu okna z 1. wykresem pojawi się drugi

plt.hist(vals2,50, density = True)
x1 = np.linspace(-1,0)
y1 = [1/3 * x + 1/3 for x in x1]
plt.plot(x1,y1, color = 'm')
x2 = np.linspace(0,2)
y2 = [1/3]*50
plt.plot(x2,y2, color = 'm')
x3 = np.linspace(2,3)
y3 = [-1/3 * x + 1 for x in x3]
plt.plot(x3,y3, color = 'm')
plt.title('100000 generated points')
plt.show()

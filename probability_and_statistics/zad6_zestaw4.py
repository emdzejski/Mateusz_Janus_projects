from random import uniform
import matplotlib.pyplot as plt
import numpy as np
def rand_volumes(n):
    vals = []
    for i in range(10000):
        x = uniform(0,2)
        vals.append(x**n)
    return vals

vol1 = rand_volumes(2)
vol2 = rand_volumes(3)
vol3 = rand_volumes(4)
vol4 = rand_volumes(5)
vol5 = rand_volumes(20)


x1 = np.linspace(0,4)
y1 = [1/4 * (x**(-1/2)) for x in x1] #funkcja gęstości
plt.hist(vol1,50,density=True) 
plt.plot(x1,y1, color = 'm')
plt.title('n = 2')
plt.show()
plt.close

x2 = np.linspace(0,8)
y2 = [1/6 * (x**(-2/3)) for x in x2]
plt.hist(vol2,50,density=True)
plt.plot(x2,y2) 
plt.title('n = 3')
plt.show()
plt.close()

x3 = np.linspace(0,16)
y3 = [1/8 * (x**(-3/4)) for x in x3]
plt.hist(vol3,50,density=True) 
plt.plot(x3,y3)
plt.title('n = 4 ')
plt.show()
plt.close()

x4 = np.linspace(0, 32)
y4 = [1/10 * (x**(-4/5)) for x in x4]
plt.hist(vol4,50,density=True) 
plt.plot(x4,y4)
plt.title('n = 5 ')
plt.show()
plt.close()

x5 = np.linspace(0,1048576)
y5 = [1/40 * (x**(-19/20)) for x in x5]
plt.hist(vol5,50,density=True) 
plt.plot(x5,y5)
plt.title('n = 20 ')
plt.show()
plt.close()



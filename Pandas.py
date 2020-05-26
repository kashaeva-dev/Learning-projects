import pandas as pd
import math
import matplotlib.pyplot as plt

x = 2
e = [i for i in range(1,10)]
y = [math.log2(i) for i in e]
z = [math.exp(i/4) for i in e]

r = 20
a = [i for i in range(37)]
xC = [r*math.sin(i*math.pi/18) for i in a]
yC = [2*r*math.cos(i*math.pi/18) for i in a]


plt.plot(xC, yC)
plt.savefig('figure.png')
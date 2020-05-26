import pandas as pd
import math
import matplotlib.pyplot as plt

x = 2
e = [i for i in range(1,10)]
y = [math.log2(i) for i in e]
z = [math.exp(i/4) for i in e]

plt.plot(e, y, z)
plt.show()
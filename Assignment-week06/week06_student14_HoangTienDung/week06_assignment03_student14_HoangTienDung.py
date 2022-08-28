import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figsize"] = [4, 6]
plt.rcParams["autolayout"] = True

def f(x):
   return np.sin(x) + x + x * np.sin(x)

x = np.linspace(-10, 10, 100)

plt.plot(x, f(x), color='red')

plt.show()
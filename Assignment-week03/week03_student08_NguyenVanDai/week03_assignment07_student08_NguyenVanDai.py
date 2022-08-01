
from __future__ import print_function
import fractions
import numpy as np
LIM = 10**6
def factor(n):
    a = np.ceil(np.sqrt(n))
    lim = min(n,LIM)
    a = np.arange(a,a+lim)
    b2 = a**2-n 
    fractions = np.modf(np.sqrt(b2))[0]
    indices = np.where(fractions == 0)
    a = np.ravel(np.take(a,indices))[0]
    a = int(a)
    b = np.sqrt(a**2-n)
    b = int(b)
    c = a+b
    d = a-b
    if c == 1 or d == 1 :
        return 
    print(c,d)
    factor(c)
    factor(d)
factor(13195)



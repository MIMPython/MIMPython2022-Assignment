import numpy as np
from matplotlib import pyplot as plt

class duongThang:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def veDuongThang(self):
        f = lambda x: self.a*x+self.b
        lb, ub = -2, 2
        x = np.linspace(lb, ub, 1001)   
        y = f(x)

        plt.subplot(1, 2, 1)
        plt.plot(x, y, '-', color='green', label='Duong thang y')
        plt.xlabel('x', fontsize=14)
        plt.ylabel('y', fontsize=14)
        plt.title('Ve duong thang', fontsize=18)
        plt.grid()
        plt.show()

if __name__=='__main__':
    y = duongThang(2,1)
    y.veDuongThang()
        



        


# if __name__=='__main__':
#     O = Circle(100)
#     O.drawCircle()
# x = [1,2,3,4]
# y = [11,22,33,44]

# fig, ax = plt.subplots(figsize=(5,5))
# O = Circle(100)
# O.voHinh()



import matplotlib.pyplot as plt
import numpy as np

#point
plt.scatter(-2,3, color = 'red')
plt.show()

#points
x_list = [1,2,3]
y_list = [2,6,1]
plt.scatter(x_list, y_list)
plt.show()

#line
plt.axis([0,20,0,20])
plt.axvline(5,0,0.5)
plt.show()

#line
plt.axis([0,20,0,20])
plt.axhline(5,0,0.5)
plt.show()

#line by points
plt.plot(x_list, y_list)
plt.show()

#cicle
ax1 = plt.subplot()
c = plt.Circle((0.5, 0.6), 0.3)
ax1.add_patch(c)
plt.show()

#retangle
ax2 = plt.subplot()
r = plt.Rectangle((0.5, 0.5), 0.2,0.5)
ax2.add_patch(r)
plt.show()




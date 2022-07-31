from math import sqrt
import matplotlib.pyplot as plt


def get_intersections(x0, y0, x1, y1, r):
    a = r/2
    h = r*sqrt(3)/2

    x2 = x0+a*(x1-x0)/r
    y2 = y0+a*(y1-y0)/r

    x3 = x2+h*(y1-y0)/r
    y3 = y2-h*(x1-x0)/r

    x4 = x2-h*(y1-y0)/r
    y4 = y2+h*(x1-x0)/r

    return ([x3, y3], [x4, y4])


def find_C():
    A = input("Nhap toa do diem A: ")
    A = list(int(x) for x in A.split(","))

    B = input("Nhap toa do diem B: ")
    B = list(int(x) for x in B.split(","))

    AB = sqrt((A[0]-B[0])**2+(A[1]-B[1])**2)
    C1, C2 = get_intersections(A[0], A[1], B[0], B[1], AB)
    print(f"Toa do diem C can tim de tam giac ABC deu la {C1} va {C2}")
    # Draw plotting
    x_axis = [[A[0], B[0]], [A[0], C1[0]], [
        A[0], C2[0]], [B[0], C1[0]], [B[0], C2[0]]]
    y_axis = [[A[1], B[1]], [A[1], C1[1]], [
        A[1], C2[1]], [B[1], C1[1]], [B[1], C2[1]]]
    for x, y in zip(x_axis, y_axis):
        plt.plot(x, y)
    plt.show()


find_C()

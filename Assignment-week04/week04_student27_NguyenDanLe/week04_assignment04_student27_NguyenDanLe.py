def dientich(a,b,c):
    x = (b[0]-a[0])*(c[1]-a[1])
    y = (c[0]-a[0])*(b[1]-a[1])
    S = 0.5*(abs(x-y))
    return S

A = (0,1)
B = (1,2)
C = (2,3)
print(dientich(A,B,C))
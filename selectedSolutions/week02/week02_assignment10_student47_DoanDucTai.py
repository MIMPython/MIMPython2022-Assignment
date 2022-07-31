from cmath import sqrt


xa = float(input ("nhập xa= "))
ya = float(input ("nhâp ya= "))
xb = float(input ("nhập xb= "))
yb = float(input ("nhâp yb= "))
def equation(a , b ,c):
    equa = list()
    equa.append((-b + sqrt((b*b - 4*a*c)))/(2*a))
    equa.append((-b - sqrt((b*b - 4*a*c)))/(2*a))
    return equa


if (xa == xb and ya == yb ):
    print ("C trùng A,B")
elif (xa == xb):
    yc = (xa**2 + ya**2 - xb**2 - yb**2)/(2*(ya-yb))
    xc1 = xb + sqrt((ya - yb)**2 - (yc - yb)**2)
    xc2 = xb - sqrt((ya - yb)**2 - (yc - yb)**2)
    print("vị trí của C là (", xc1, ", ", yc, ") (", xc2, ", ", yc, ")" )
elif (ya == yb):
    xc = (xa**2 + ya**2 - xb**2 - yb**2)/(2*(xa - xb))
    yc1 = yb + sqrt((xa - xb)**2 - (xc - xb)**2)
    yc2 = yb - sqrt((xa - xb)**2 - (xc - xb)**2)
    print("vị trí của C là (", xc, ", ", yc1, ") (", xc, ", ", yc2, ")" )
else: 
    a = (xa**2 + ya**2 - xb**2 - yb**2)/(2*(xa-xb)) -xb
    b = (yb - ya)/(xa - xb)
    an = b**2 + 1 
    bn = 2*b*a - 2*yb
    cn = -(xa - xb)**2 - (ya - yb)**2 + a**2 + yb**2
    yc = equation(an, bn,cn)
    yc1 = yc[0]
    yc2 = yc[1]
    xc1 = a + xb + b*yc1
    xc2 = a + xb + b*yc2
    print ("vị trí của C là (", xc1, ", ", yc1, ") (", xc2, ", ", yc2, ")" )
    

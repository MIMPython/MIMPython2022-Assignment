from math import sqrt
from xml.etree.ElementTree import C14NWriterTarget


a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
if (a == 0 and b == 0 and c == 0):
    print("vô số nghiệm")
elif (a == 0 and b == 0 ):
    print("vô nghiệm")
elif (a == 0):
    print((-c/b),",",sep = "")
elif (b*b - 4*a*c > 0):
    print ((-b + sqrt((b*b - 4*a*c)))/(2*a), ", ",(-b - sqrt((b*b - 4*a*c)))/(2*a), sep = "")
elif ( b*b - 4*a*c == 0 ):
    print((-b/(2*a)),",", sep = "" )
else: print("vô nghiệm")
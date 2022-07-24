import math
print ("Nhập hệ số của tam thức bậc 2 vào đây:")
a = int(input())
b = int(input())
c = int(input())
delta = b**2 - 4*a*c

if delta >0:
	x_1 = (-b + math.sqrt(delta))/(2*a)
	x_2 = (-b - math.sqrt(delta))/(2*a)

	print("Nghiệm của phương trình",a,"x^2","+",b,"x","+",c,"là:"\
	,x_1,"và",x_2)

elif delta == 0:
	x = -b/(2*a)
	print("Nghiệm của phương trình",a,"x^2","+",b,"x","+",c,"là:",x)

else:
	print('Phương trình',a,"x^2","+",b,"x","+",c,"vô nghiệm.")
def triangeArea(x1,y1,x2,y2,x3,y3):
  Triange_Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
  print("Diện tích là :",Triange_Area)
  if Triange_Area == 0:
    print("Không là một tam giác!")
 
 
x1 = int(input("Nhập x1 :"))
y1 = int(input("Nhập y1 :"))
x2 = int(input("Nhập x2 :"))
y2 = int(input("Nhập y2 :"))
x3 = int(input("Nhập x3 :"))
y3 = int(input("Nhập y3 :"))
 

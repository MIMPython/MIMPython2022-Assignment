import math
import datetime
def perimeter(x):
    h=0
    m=0
    s=0
    while x>60:
      h=x//3600
      m=(x-h*3600)//60
      x=x-m*60-h*3600
    s=x
    h=(h+m/60+s/3600)/12*360 
    m=(m+s/60)/60*360
    s=s*6
    M=math.sqrt(2-2*math.cos((h-m)*math.pi/180)) + math.sqrt(2-2*math.cos((m-s)*math.pi/180)) + math.sqrt(2-2*math.cos((s-h)*math.pi/180))
    return M

def changeTime(x):
    h=0
    m=0
    s=0
    while x>60:
      h=x//3600
      m=(x-h*3600)//60
      s=x-m*60-h*3600
      x=x-m*60-h*3600
    print(h,"h",m,"m",s,"s")
Max=-1
Min=10000 
for i in range(10,43190,1):
    Max=max(Max,perimeter(i))
    Min=min(Min,perimeter(i))
print("Giá trị lớn nhất của M:",Max)
print("Giá trị nhỏ nhất của M:",Min)
print("Các thời điểm M đạt giá trị Max: ")
for i in range(10,43190,1):
    if(perimeter(i)==Max):
        changeTime(i)
print("Các thời điểm M đạt giá trị Min: ")
for i in range(10,43190,1):
    if(perimeter(i)==Min):
        changeTime(i)
from week04_assignment02_student56_HoangTuanTu import Point

def area(line):
    l1,l2,l3 = map(float,line)
    p = sum(line)/2
    return (p*(p-l1)*(p-l2)*(p-l3))**(1/2)

if __name__ == "__main__":
    triangle  = []
    line = []
    for i in range(3):
        print("Input x and y of {} point (Ex: 2 3)".format(chr(i+65)),end=": ")
        x,y = map(float,input().split())
        point = Point(x,y)
        triangle.append(point)
    for i in range(3):
        line.append(triangle[1].distance(triangle[2],metric="L2"))
    
    print("Area of your triangle is:",area(line))
import math
import turtle

def drawShape(points): #Vẽ hình tam giác
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    turtle.penup()
    turtle.goto(x1 * 100, x2 * 100) #Gấp lên 100 cho hình nó to
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(x2 * 100, y2 * 100)
    turtle.goto(x3 * 100, y3 * 100)
    turtle.goto(x1 * 100, x2 * 100)
    turtle.end_fill()
    turtle.penup()
    
def equilateralTriangle(A, B): #Tìm điểm C
    x1 = ((A[0] + B[0]) + math.sqrt(3)*(B[1]-A[1]))/2
    y1 = ((B[1] + A[1]) - math.sqrt(3)*(B[0]-A[0]))/2
    x2 = ((A[0] + B[0]) - math.sqrt(3)*(B[1]-A[1]))/2
    y2 = ((B[1] + A[1]) + math.sqrt(3)*(B[0]-A[0]))/2
    return [(x1, y1), (x2, y2)]

def main():
    A = (-3, 4)
    B = (4, 2)
    C = equilateralTriangle(A, B)
    print (f"Toạ độ điểm C là ({C[0]} và {C[1]}")
    triangle = [A, B, C[0]]
    drawShape(triangle)
    turtle.done()
main()
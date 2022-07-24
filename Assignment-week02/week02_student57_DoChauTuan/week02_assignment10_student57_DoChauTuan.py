import math
def coordinate(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False
    else:
        x = (x1 + x2 + math.sqrt(3)*(y1 - y2))/2
        y = (y1 + y2 + math.sqrt(3)*(x2 - x1))/2
        return (x, y)
if __name__ == "__main__":
    print(coordinate(0, 0, 2, 0)) # (1.0, 1.7320508075688772) = (1, sqrt(3))
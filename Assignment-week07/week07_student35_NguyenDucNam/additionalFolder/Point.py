import math 
class Point: 

    def __init__(self,x,y):
        """Initialize attributes to a point."""
        self.x = x
        self.y = y
        
    def distance(self, other, metric):
        """Calculate distance between any two points."""
        if metric == 'L2':
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        if metric == 'L1': 
            return abs(self.x-other.x)+abs(self.y-other.y)
    def getSymmetry(self): 

        """Create a point of symmetry."""
        return -self.x, -self.y

    def __repr__(self):
        """Show points in string."""
        return 'x=' + str(self.x) + ';' + 'y=' + str(self.y)
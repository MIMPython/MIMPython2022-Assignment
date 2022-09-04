from fractions import Fraction
class Fractions:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Fraction({},{})'.format(self.x,self.y)
    def fraction(self):
        return Fraction(self.x,self.y)
    
    def initializeFromFloat(a):
        return Fraction(a)

if __name__=='__main__':
    a= Fractions.initializeFromFloat('0.1')
    print(a.__repr__())






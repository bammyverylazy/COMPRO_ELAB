import math
class Fraction :
    def __init__(self,numerator,denominator):
        simpl = math.gcd(numerator,denominator)
        if numerator == 0:
            denominator = 1
        else:
            self.numerator= numerator/simpl
            self.denominator = denominator/simpl
    def evaluate(self):
        return self.numerator/self.denominator
    def add(self,n):
        pass
    def __add__(self, other):
        pass
    
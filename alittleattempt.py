from math import *
import matplotlib.pyplot as plt
import numpy as np


class Father:
    def __init__(self, a):
        # self.hw()
        print(a)
        pass

    def hw(self):
        print("HalloWorld")


class Children(Father):
    def hw(self):
        print("No")


# f = Father()
# c = Children()
# c.__init__()

if __name__ == "__main__":
    # print('HalloWorld')
    # f = Father('114514')
    # f.__init__(55644)
    c = Children(123)


class Rectangular:
    def __init__(self, LongSideLength, ShortSideLength):
        self.a = LongSideLength
        self.b = ShortSideLength
        self.area = self.a * self.b

    def returnmyself(self):
        return self


rec1 = Rectangular(11, 8).returnmyself()
rec2 = Rectangular(rec1.a, 12)

rec1 = Rectangular(11, 8)
pass
rec2 = Rectangular(20, 6)
pass


class Rectangular:
    a = 1
    b = 1
    area = 1

    def init(self, LongSideLength, ShortSideLength):
        self.a = LongSideLength
        self.b = ShortSideLength
        self.area = self.a * self.b
        return self


rectest = Rectangular()
rec1 = rectest.init(11, 8)
pass
rec2 = rectest.init(20, 6)
pass

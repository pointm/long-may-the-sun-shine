from math import *
import matplotlib.pyplot as plt
import numpy as np


class Father():
    def __init__(self, a):
        # self.hw()
        print(a)
        pass

    def hw(self):
        print('HalloWorld')


class Children(Father):
    def hw(self):
        print('No')


# f = Father()
# c = Children()
# c.__init__()

if __name__ == '__main__':
    # print('HalloWorld')
    f = Father('114514')
    f.__init__(55644)

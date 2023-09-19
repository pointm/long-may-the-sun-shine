class Father():
    def __init__(self):
        self.hw()
        return
    def hw(self):
        print('HalloWorld')

class Children(Father):
    def hw(self):
        print('No')

f = Father()
c = Children()
c.__init__()
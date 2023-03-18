class Mytime:
    def __init__(self,h,m,s):
        self.h = h
        self.m = m
        self.s = s

    def plus(self):
        self.s += 1
        if self.s >= 60:
            self.m += 1
            self.s -= 60
        
        if self.m >= 60:
            self.h += 1
            self.m -= 60
    
    def minus(self):
        self.s -= 1
        if self.s <= 0:
            self.m -= 1
            self.s += 60

        if self.m <= 0:
            self.h -= 1
            self.m += 60
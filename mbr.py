import math
class mbr:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def fromstring(str1):
        arr=str1.split(",")
        return mbr(float(arr[0]),float(arr[1]),float(arr[2]),float(arr[3]))

    def dist2p(self,x,y):
        xd=min(abs(x-self.x1),abs(x-self.x2))
        if self.x1<x and self.x2>x:
            xd=0
        yd=min(abs(x-self.y1),abs(x-self.y2))
        if self.y1<y and self.y2>y:
            yd=0
        return math.sqrt(xd*xd+yd*yd)
    def dist2mbr(self,other):
        ans=0
        d=0
        if other.x2 < self.x1:
            d=self.x1-other.x2
        elif self.x2 < other.x1:
            d=other.x1-self.x2
        ans+=d*d
        d = 0
        if other.y2 < self.y1:
            d = self.y1 - other.y2
        elif self.y2 < other.y1:
            d = other.y1 - self.y2
        ans += d * d
        return ans
    def moddist(self,other):
        m=(self.x1+self.x2-other.x1-other.x2)*(self.x1+self.x2-other.x1-other.x2)/4+(self.y1+self.y2-other.y1-other.y2)*(self.y1+self.y2-other.y1-other.y2)/4
        return self.dist2mbr(other)+0.1*m
    def strdis(str1,str2):
        mbr1=mbr.fromstring(str1)
        mbr2=mbr.fromstring(str2)
        return mbr1.moddist(mbr2)
    def __str__(self):
        return str(self.x1)+","+str(self.x2)+","+str(self.y1)+","+str(self.y2)
    def __cmp__(self, other):
        return 0


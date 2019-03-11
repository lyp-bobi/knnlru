from LRUCache import LRUCache
from kNNLRUCache import kNNLRUCache
import threading
class queueManager:
    def __init__(self,inputmbrs):
        self.qu1= kNNLRUCache(100)
        self.qu2= LRUCache(100)
        self.mbrs=inputmbrs
        self.hit1=0
        self.miss1=0
        self.hit2 = 0
        self.miss2 = 0

    def getSpatial(self,x,y,r):
        threadList = []
        def thread_process(mbr1,x1,y1,r1):
            if mbr1.dist2p(x1,y1) < r1:
                result1=self.qu1.get(str(mbr1))
                if result1 ==-1:
                    self.miss1+=1
                    self.qu1.set(str(mbr1),0)
                else:
                    self.hit1+=1
                result2 = self.qu2.get(str(mbr1))
                if result2 == -1:
                    self.miss2 += 1
                    self.qu2.set(str(mbr1),0)
                else:
                    self.hit2 += 1
                if result1!=result2:
                    print("different!")
        for mbr in self.mbrs:
            th = threading.Thread(target=thread_process, args=(mbr,x,y,r))
            threadList.append(th)
            th.start()


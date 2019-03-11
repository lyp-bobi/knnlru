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
        for mbr in self.mbrs:
            if mbr.dist2p(x,y) < r:
                result1=self.qu1.get(str(mbr))
                if result1 ==-1:
                    self.miss1+=1
                    self.qu1.set(str(mbr),0)
                else:
                    self.hit1+=1
                result2 = self.qu2.get(str(mbr))
                if result2 == -1:
                    self.miss2 += 1
                    self.qu2.set(str(mbr),0)
                else:
                    self.hit2 += 1
                if result1!=result2:
                    print("different!")
        # def thread_process(mbr):
        #     if mbr.dist2p(x,y) < r:
        #         print("checking" + str(mbr))
        #         result1=self.qu1.get(str(mbr))
        #         if result1 ==-1:
        #             self.miss1+=1
        #             self.qu1.set(str(mbr),0)
        #         else:
        #             self.hit1+=1
        #         result2 = self.qu2.get(str(mbr))
        #         if result2 == -1:
        #             self.miss2 += 1
        #             self.qu2.set(str(mbr),0)
        #         else:
        #             self.hit2 += 1
        #         if result1!=result2:
        #             print("different!")
        # for mbr in self.mbrs:
        #     threadList=[]
        #     th = threading.Thread(target=thread_process, args=(mbr,))
        #     threadList.append(th)
        #     th.start()
        #
        # th.join()
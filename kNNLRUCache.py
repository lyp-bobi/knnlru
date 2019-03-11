from cacheQueue import cacheQueue
from mbr import mbr
from queue import PriorityQueue
class knnlist:
    def __init__(self,mbrstr,k):
        self.mbrstr=mbrstr
        self.k=k
        self.list=[]

    def tryinsert(self,mbrstr):
        if len(self.list)<self.k:
            self.list.append((mbr.strdis(mbrstr,self.mbrstr),mbrstr))
        else:
            self.list.append((mbr.strdis(mbrstr,self.mbrstr),mbrstr))
            self.list.sort(key=lambda t:t[0],reverse=True)
            self.list.pop(0)
            #print(self.list)
        
class kNNLRUCache(cacheQueue):

    # @param capacity, an integer
    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity
        self.knn_list={}
        self.k=3

    # @return an integer
    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                for (dist,mbrstri) in self.knn_list[key].list:
                    if mbrstri in self.used_list:
                        #print(mbrstri)
                        self.used_list.remove(mbrstri)
                        self.used_list.append(mbrstri)
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value
        self.knn_list[key]= knnlist(key,self.k)
        for mbrstr in self.cache:
            if mbrstr!=key:
                self.knn_list[key].tryinsert(mbrstr)
                self.knn_list[mbrstr].tryinsert(key)




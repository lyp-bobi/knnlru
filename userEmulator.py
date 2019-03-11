from queueManager import queueManager
from multiprocessing.dummy import Pool as ThreadPool
from visitor import visitor
from mbr import mbr

mbrs=[]
f = open('mbrs.txt', 'r')
line = f.readline()
while line:
    spt=line.split(",")
    mbrs.append(mbr(float(spt[0]),float(spt[1]),float(spt[2]),float(spt[3])))
    line = f.readline()

f.close()
global QuMng
QuMng=queueManager(mbrs)
sum=0
for j in range(100):#num of tests
    def process(mm):
        global QuMng
        vis = visitor(QuMng)
        vis.visit()
    items=range(3)#num of users
    pool = ThreadPool()
    pool.map(process, items)
    pool.close()
    pool.join()


    print(QuMng.hit1,QuMng.miss1,QuMng.hit1*1.0/(QuMng.hit1+QuMng.miss1))
    print(QuMng.hit2,QuMng.miss2,QuMng.hit2*1.0/(QuMng.hit2+QuMng.miss2))
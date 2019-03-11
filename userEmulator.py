from queueManager import queueManager
import threading
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
    threadList = []
    def thread_process():
        global QuMng
        vis = visitor(QuMng)
        vis.visit()
    for tid in range(3):#num of users
        th = threading.Thread(target=thread_process, args=())
        threadList.append(th)
        th.start()

    th.join()

    print(QuMng.hit1,QuMng.miss1,QuMng.hit1*1.0/(QuMng.hit1+QuMng.miss1))
    print(QuMng.hit2,QuMng.miss2,QuMng.hit2*1.0/(QuMng.hit2+QuMng.miss2))
import time
import random
from sklearn.datasets.samples_generator import make_classification
class visitor:
    def __init__(self,q):
        self.quMng=q
        self.last = (0, 0, 0)
    def visit(self):
        time.sleep(random.random())
        X1, Y1 = make_classification(n_samples=400, n_features=2, n_redundant=0,
                                     n_clusters_per_class=1, n_classes=4)
        for row in X1:
            self.quMng.getSpatial(row[0]*5-167,row[1]*76,random.random()*0.001)
        # for i in range(200):
        #     if random.random()<0.05:
        #         x=random.random()*5-167
        #         y=random.random()*76
        #         r=random.random()*0.01
        #     else:
        #         x = self.last[0]+(random.random()-0.5)*0.1
        #         y = self.last[1]+(random.random()-0.5)*0.1
        #         r = self.last[2]+(random.random()-0.5)*0.01
        #     self.last=(x,y,r)
        #     self.quMng.getSpatial(x,y,r)


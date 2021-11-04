import time

import multiprocessing as mp
A=[1,2,3,4,5,6]*100

def carre(x):
    return x**50000
t=time.time()
L=[]
for i in A:
    L.append(carre(i))

print(time.time()-t)


t=time.time()
list(mp.Pool(5).map(carre,A))
print(time.time()-t)
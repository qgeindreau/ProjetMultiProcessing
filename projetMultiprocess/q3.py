#!/usr/bin/python3
import time

t = time.time()

import multiprocessing as mp
from q2 import Annagrameur

class T_mt3(mp.Process):
    def __init__(self,nb,num):
        mp.Process.__init__(self)
        self.n = nb #nb threads,q
        self.nu = num #numero du thread 

    def run(self) :
        res=[]
        while not qe.empty():
            res+=Annagrameur(qe.get()).anag_list()
        qs.put(res)

    


if __name__ == "__main__":
    L=[]
    t=time.time()
    with open('words', 'r') as f:
        list_mots = f.read().split('\n')
    dico={}
    qe=mp.Queue()
    for i in list_mots:
        dico.setdefault(len(i), []).append(i)
    for key in dico.keys():
        qe.put(dico[key])
    t=time.time()
    nb=3
    qs=mp.Queue()
    tasks=[T_mt3(nb,i+1) for i in range(nb)]
    for i in tasks:
        i.start()
        i.run()
    for i in tasks:
        i.join()
    print(qe.empty())
    while not qs.empty():
        L+=qs.get()
    with open('result/q3.result', 'w') as f:
        for annagrammes in L:
            f.write(str(annagrammes)[1:-1])
            f.write('\n')
    print('Temps pour générer le fichier q3.result :', time.time() - t)
    maxgrp = max(len(grp) for grp in L)
    lens = [len(i) for i in L]
    for size in range(1, maxgrp + 1):
        print('Il y a {nb} groupe de {size} mots'.format(nb=lens.count(size),
                                                         size=size))
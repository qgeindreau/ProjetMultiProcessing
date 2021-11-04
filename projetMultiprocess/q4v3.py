#!/usr/bin/python3
import time
import multiprocessing as mp
import pathos

def primatize(word):
    #On passe cette fonction en globale pour pouvoir l utiliser en multiprocessing
    if word == '':
        return 1
    min = "azertyuiopqsdfghjklmwxcvbn0123456789-.'&,/!"
    maj = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
    primenumbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191
    ]
    try:
        return primatize(word[1:]) * primenumbers[min.index(word[0])]
    except:
        return primatize(word[1:]) * primenumbers[maj.index(word[0])]


class Annagrameur:
    def __init__(self, liste, nb_proc):
        self.list_mots = liste
        self.nb_proc = nb_proc


    def encode(self):
        with pathos.pools.ProcessPool() as exec:
            enc_zip = zip(exec.map(primatize, self.list_mots), self.list_mots)
            print('temps après encodage:', time.time() - t)
        result = {}
        for i in enc_zip:
            result.setdefault(i[0], []).append(i[1])
        print('Temps apres inversion', time.time() - t)
        return result

    def anag_list(self):
        return self.encode().values()


if __name__ == "__main__":
    t = time.time()
    with open('words', 'r') as f:
        list_mots = f.read().split('\n')
    print('Temps chargement fichier', time.time() - t)
    worker = Annagrameur(list_mots, 8)
    res = worker.anag_list()
    with open('result/q3v3.result', 'w') as f:
        for annagrammes in res:
            f.write(str(annagrammes)[1:-1])
            f.write('\n')
    print('Temps pour générer le fichier q3v3.result :', time.time() - t)
    maxgrp = max(len(grp) for grp in res)
    lens = [len(i) for i in res]
    for size in range(1, maxgrp + 1):
        print('Il y a {nb} groupe de {size} mots'.format(nb=lens.count(size),
                                                         size=size))
#!/usr/bin/python3
import time

dic=dict(zip("azertyuiopqsdfghjklmwxcvbn0123456789-.'&,/!",[
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191
    ]))|dict(zip('AZERTYUIOPQSDFGHJKLMWXCVBN',[
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101]))

class Annagrameur:
    def __init__(self, liste):
        self.list_mots = liste

    def encode(self):
        def primatize(word):
            try:
                return dic[word[0]]*primatize(word[1:])
            except:
                try:
                    return dic[word[0]]
                except:
                    return 1
        return {mot: primatize(mot) for mot in self.list_mots}

    def anag_list(self):
        class ReversibleDict(dict):
            def reversed(self):
                new_dict = {}
                for k, v in self.items():
                    new_dict.setdefault(v, []).append(k)
                return new_dict

        return list(ReversibleDict(self.encode()).reversed().values())


if __name__ == "__main__":
    t = time.time()
    with open('words', 'r') as f:
        list_mots = f.read().split('\n')
    worker = Annagrameur(list_mots)
    res = worker.anag_list()
    with open('result/q2.result', 'w') as f:
        for annagrammes in res:
            f.write(str(annagrammes)[1:-1])
            f.write('\n')
    print('Temps pour générer le fichier q2.result :', time.time() - t)
    maxgrp = max(len(grp) for grp in res)
    lens = [len(i) for i in res]
    for size in range(1, maxgrp + 1):
        print('Il y a {nb} groupe de {size} mots'.format(nb=lens.count(size),
                                                         size=size))
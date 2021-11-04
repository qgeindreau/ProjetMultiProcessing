#!/usr/bin/python3
import time
t=time.time()

class Annagrameur:
    def __init__(self, liste):
        self.list_mots = liste

    def encode(self):
        def minusculize(word):
            if word == '': return ''
            min = 'azertyuiopqsdfghjklmwxcvbn'
            maj = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
            if maj.find(word[0]) != -1:
                return min[maj.index(word[0])] + minusculize(word[1:])
            else:
                return word[0] + minusculize(word[1:])

        return {
            mot: frozenset(
                str(minusculize(mot).count(lettre)) + lettre
                for lettre in set(minusculize(mot)))
            for mot in self.list_mots
        }

    def anag_list(self):
        class ReversibleDict(dict):
            def reversed(self):
                new_dict = {}
                for k, v in self.items():
                    new_dict.setdefault(v, []).append(k)
                return new_dict

        return list(ReversibleDict(self.encode()).reversed().values())


if __name__ == "__main__":
    with open('words', 'r') as f:
        list_mots = f.read().split('\n')
    worker = Annagrameur(list_mots)
    res = worker.anag_list()
    with open('result/q1.result', 'w') as f:
        for annagrammes in res:
            f.write(str(annagrammes)[1:-1])
            f.write('\n')
    print('Temps pour générer le fichier q1.result :', time.time() - t)
    maxgrp = max(len(grp) for grp in res)
    lens = [len(i) for i in res]
    for size in range(1, maxgrp + 1):
        print('Il y a {nb} groupe de {size} mots'.format(nb=lens.count(size),
                                                         size=size))
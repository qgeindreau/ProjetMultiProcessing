import time
import ray
import numpy as np

class ReversibleDict(dict):
    def reversed(self):
        new_dict = {}
        for k, v in self.items():
            new_dict.setdefault(v, []).append(k)
        return new_dict

dic=dict(zip("azertyuiopqsdfghjklmwxcvbn0123456789-.'&,/!",[
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
        149, 151, 157, 163, 167, 173, 179, 181, 191
    ]))|dict(zip('AZERTYUIOPQSDFGHJKLMWXCVBN',[
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97, 101]))
def primatize(word):
    try:
        return dic[word[0]]*primatize(word[1:])
    except:
        try:
            return dic[word[0]]
        except:
            return 1


@ray.remote
def lprimatize(liste):
    return zip(liste, map(primatize, liste))


if __name__ == "__main__":
    ray.init()
    t = time.time()
    with open('words', 'r') as f:
        list_mots = f.read().split('\n')
    a = np.array_split(list_mots, 8)
    dico = ReversibleDict()
    for i in map(ray.get, map(lprimatize.remote, a)):
        dico.update(i)
    res = dico.reversed().values()
    with open('result/q4.result', 'w') as f:
        for annagrammes in res:
            f.write(str(annagrammes)[1:-1])
            f.write('\n')
    print('Temps pour générer le fichier q4.result :', time.time() - t)
    maxgrp = max(len(grp) for grp in res)
    lens = [len(i) for i in res]
    for size in range(1, maxgrp + 1):
        print('Il y a {nb} groupe de {size} mots'.format(nb=lens.count(size),
                                                         size=size))
from multiprocessing.connection import Listener
from multiprocessing import Pool


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


address = ('localhost', 6050)

listener= Listener(address, authkey=b'secret password')
with listener.accept() as conn:
    data = conn.recv()
    reponse=dict(zip(data,Pool(10).map(primatize,data)))
    conn.send(reponse)

import collections
import random
from busca_profundidade import profundidade

def ciclo(G, a, ce):
    while(True):
        vo = random.choice(a)
        while vo not in ce:
            vo = random.choice(a)
        vd = random.choice(a)
        while vd == vo:
            vd = random.choice(a)
            
        c = profundidade(G, vo, vd)
        if c == 0:
            continue
        if len(c) < 3:
            vk = random.choice(a)
            while vk == vo and vk != vd:
                vk = random.choice(a)
            c2 = profundidade(G, vd, vk)
            c.remove(vd)
            aux = profundidade(G, vd, vk)
            if aux == 0:
                continue
            c += aux
            vd = vk

        c.remove(vd)
        aux = profundidade(G, vd, vo)
        if aux == 0:
            continue
        c += aux

        aux = collections.Counter(c)
        repet = [i for i in aux if aux[i]>1]
        if len(repet) == 1 and len(c) > 3 and aux[repet[0]] == 2:
            break
    return c
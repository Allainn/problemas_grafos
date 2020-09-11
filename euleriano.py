import random
import copy
from ciclo import ciclo
from pontes import pontes

NAO_EULERIANO = 0
EULERIANO = 1
SEMI_EULERIANO = 2

RESULTS = {
    0: 'NÃO EULERIANO',
    1: 'EULERIANO',
    2: 'SEMI EULERIANO'
}

def verifica_euleriano(G):
    result = 0
    impar = 0
    for v in G.keys():
        if G[v].__len__() % 2 != 0:
            impar += 1
        if impar > 2:
            return result

    if impar == 0:
        result = EULERIANO
    elif impar == 2:
        result = SEMI_EULERIANO

    return result

def hierholzer(G):
    V = list(G.keys())
    ce = [random.choice(V)]
    Gred = copy.deepcopy(G)
    
    while Gred:
        c = ciclo(Gred, V, ce)
        for i in range(len(c)-1):
            Gred[c[i]].pop(c[i+1])
            Gred[c[i+1]].pop(c[i])
            if len(Gred[c[i]]) == 0:
                V.remove(c[i])
                Gred.pop(c[i])
            if len(Gred[c[i+1]]) == 0:
                V.remove(c[i+1])
                Gred.pop(c[i+1])
                
        i = ce.index(c[0])
        ce.remove(c[0])
        ce[i:i] = c
            
    return ce

def fleury(G):
    Gred = copy.deepcopy(G)
    V = list(Gred.keys())
    ver = verifica_euleriano(Gred)
    if ver == EULERIANO:
        vc = random.choice(V)
    elif ver == SEMI_EULERIANO:
        for v in V:
            if len(G[v])%2 != 0:
                vc = v
                break
    else:
        return 0
    ce = [vc]
    while len(Gred[vc]) > 0:
        if len(Gred[vc]) == 1:
            vadj = list(Gred[vc].keys())[0]
        else:
            p = pontes(Gred)
            for vadj in Gred[vc].keys():
                if (vc, vadj) not in p:
                    break
        ce.append(vadj)
        Gred[vc].pop(vadj)
        Gred[vadj].pop(vc)
        vc = vadj
    return ce
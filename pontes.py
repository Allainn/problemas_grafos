from componentes_conexos import UGRAPHconComps
import copy

def pontes(G):
    A = []
    C = []
    for v in G.keys():
        for a in G[v].keys():
            A.append((v, a))
    a = UGRAPHconComps(G)
    for i in A:
        Gred = copy.deepcopy(G)
        Gred[i[0]].pop(i[1])
        Gred[i[1]].pop(i[0])
        b = UGRAPHconComps(Gred)
        if b > a:
            C.append(i)
    return C
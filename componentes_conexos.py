# https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/components.html

cc = {}
def dfsRconComps(G, v, id):
    cc[v] = id
    for a in G[v].keys():
        if cc[a] == -1:
            dfsRconComps(G, a, id)

def UGRAPHconComps(G):
    id = 0
    V = list(G.keys())
    for v in V:
        cc[v] = -1
    for v in V:
        if(cc[v] == -1):
            id+=1
            dfsRconComps(G, v, V[id])
        
    return id
def printCaminho(pai, vo, vd):
    if vo == vd:
        print(vo, end='\t')
    elif pai[vo, vd] == None:
        print("Não exite caminho do vértice {} ao vértice {}".format(vo, vd))
    else:
        printCaminho(pai, vo, pai[vo,vd])
        print(vd, end='\t')

def peso_arv(garv, G):
    soma = 0
    for i, j in garv:
        soma += G[i][j]
    return soma

def quicksort_kruskal(fv, G):
    if len(fv) <= 1: return fv
    m = G[fv[0][0]][fv[0][1]]
    return quicksort_kruskal([(i,j) for i, j in fv if G[i][j] < m], G) + \
        [(i,j) for i, j in fv if G[i][j] == m] + \
        quicksort_kruskal([(i,j) for i, j in fv if G[i][j] > m], G)

def acharConj(v, conj):
    while conj[v] != v:
        v = conj[v]
    return v

def juntarConjs(conjVi, conjVj, tamConj, conj):
    if tamConj[conjVj] > tamConj[conjVi]:
        conj[conjVi] = conj[conjVj]
        tamConj[conjVj] = tamConj[conjVj] + tamConj[conjVi]
        tamConj[conjVi] = 0
    else:
        conj[conjVj] = conj[conjVi]
        tamConj[conjVi] = tamConj[conjVi] + tamConj[conjVj]
        tamConj[conjVj] = 0

def kruskal(G):
    conj = {}
    tamConj = {}
    V = G.keys()
    L = []
    for v in V:
        conj[v] = v
        tamConj[v] = 1
        for a in G[v].keys():
            if (a,v) in L:
                continue
            L.append((v,a))

    Arv = []
    tam = len(V)

    while L:
        L = quicksort_kruskal(L, G)
        vi, vj = L.pop(0)
        conjVi = acharConj(vi, conj)
        conjVj = acharConj(vj, conj)
        if conjVi != conjVj:
            Arv.insert(0, (vi, vj))
            juntarConjs(conjVi, conjVj, tamConj, conj)
        elif tamConj[conjVi] == tam or tamConj[conjVj] == tam:
            break
    
    return Arv

def quicksort_prim(fv, p):
    if len(fv) <= 1: return fv
    m = p[fv[0]]
    return quicksort_prim([i for i in fv if p[i] < m], p) + \
        [i for i in fv if p[i] == m] + \
        quicksort_prim([i for i in fv if p[i] > m], p)

def prim(G, vo):
    parv = {}
    pai = {}
    Fv = list(G.keys())
    for v in Fv:
        parv[v] = float('inf')
        pai[v] = None

    parv[vo] = 0
    vpm = 0
    arv = []
    while Fv:
        Fv = quicksort_prim(Fv, parv)
        vpm = Fv.pop(0)
        arv.append((pai[vpm], vpm))
        for vadj in G[vpm]:
            if vadj in Fv and G[vpm][vadj] < parv[vadj]:
                parv[vadj] = G[vpm][vadj]
                pai[vadj] = vpm
    arv.pop(0)
    return arv, sorted(pai.items()), sorted(parv.items())
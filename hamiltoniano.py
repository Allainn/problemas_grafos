from math import ceil
import copy

def aresta_n_adjacentes(G):
    A = []
    Vs = list(G.keys())
    for i in Vs:
        aux = list(G[i].keys())
        for v in Vs:
            if v not in aux and v != i:
                if (v, i) not in A and (i, v) not in A: 
                    A.append((i, v))
    return A

def validar(flag):
    if flag:
        print("Grafo Hamiltoniano")
    else:
        print("Grafo pode não ser Hamiltoniano")

def ore(G):
    Vs = list(G.keys())
    n = len(Vs)
    if n < 3:
        print("Não é Halmitoniano")
    
    A = aresta_n_adjacentes(G)

    flag = True
    n = len(Vs)
    print(n)
    for a in A:
        print(a, len(G[a[0]])+len(G[a[1]]))
        if len(G[a[0]])+len(G[a[1]]) < n:
            flag = False
            break
    
    validar(flag)
    

def dirac(G):
    Vs = list(G.keys())
    n = len(Vs)
    if n < 3:
        print("Não é Halmitoniano")

    n = ceil(n/2)
    flag = True
    print(n)
    for v in Vs:
        print(len(G[v]))
        if len(G[v]) < n:
            flag = False
            break
            
    validar(flag)

def bandy_chvatal(G):
    Vs = list(G.keys())
    n = len(Vs)
    if n < 3:
        print("Não é Halmitoniano")
    
    A = aresta_n_adjacentes(G)

    G_copy = copy.deepcopy(G)
    n = len(Vs)
    while A:
        flag = False
        for a in A:
            if len(G_copy[a[0]])+len(G_copy[a[1]]) >= n:
                G_copy[a[0]][a[1]] = 1
                G_copy[a[1]][a[0]] = 1
                A.remove(a)
                flag = True
                break
        if not(flag):
            break
            
    flag = True
    for v in Vs:
        if len(G_copy[v]) < n-1:
            flag = False
            break
            
    validar(flag)
def extrairMin(Fv, pc):
    mn = float('inf')
    mi = 0
    for i in Fv:
        if pc[i] < mn:
            mi = i
            mn = pc[i]
    Fv.remove(mi)
    return mi

def dijkstra(G, vo):
    pc = {}
    pai = {}
    Fv = list(G.keys())
    for v in Fv:
        pc[v] = float('inf')
        pai[v] = None

    pc[vo] = 0
    vpm = 0
    while Fv:
        vpm = extrairMin(Fv, pc)
        for vadj in G[vpm]:
            if pc[vadj] > pc[vpm] + G[vpm][vadj]:
                pc[vadj] =  pc[vpm] + G[vpm][vadj]
                pai[vadj] = vpm
                
    return sorted(pc.items()), sorted(pai.items())

def dfs_visit(vd, Lv, marca, G):
    marca[vd] = 'D'
    for vadj in G[vd]:
        if marca[vadj] == 'I':
            dfs_visit(vadj, Lv, marca, G)
    marca[vd] = 'E'
    
    Lv.insert(0, vd)

def ordTopologica(G):
    marca = {}
    V = list(G.keys())
    for v in V:
        marca[v] = 'I'
    
    Lv = []
    for v in V:
        if marca[v] == 'I':
            dfs_visit(v, Lv, marca, G)
            
    return(Lv)

def cm_ordTopologica(G, vo):
    pc = {}
    pai = {}
    for v in G.keys():
        pc[v] = float('inf')
        pai[v] = None

    pc[vo] = 0
    Lv = ordTopologica(G)
    
    while Lv:
        vpm = Lv.pop(0)
        for vadj in G[vpm]:
            if pc[vadj] > pc[vpm] + G[vpm][vadj]:
                pc[vadj] =  pc[vpm] + G[vpm][vadj]
                pai[vadj] = vpm

    return sorted(pc.items()), sorted(pai.items())

def bellmanFord(G, vo):
    pc = {}
    pai = {}
    V = list(G.keys())
    for v in V:
        pc[v] = float('inf')
        pai[v] = None
        
    pc[vo] = 0
    
    for _ in range(len(G)):
        atualizacao = False
        for vpai in V:
            for vadj in G[vpai]:
                if pc[vadj] > pc[vpai] + G[vpai][vadj]:
                    pc[vadj] =  pc[vpai] + G[vpai][vadj]
                    pai[vadj] = vpai
                    atualizacao = True
        if not(atualizacao):
            break
    
def bellmanFord(G, vo):
    pc = {}
    pai = {}
    V = list(G.keys())
    for v in V:
        pc[v] = float('inf')
        pai[v] = None
        
    pc[vo] = 0
    
    for _ in range(len(G)):
        atualizacao = False
        for vpai in V:
            for vadj in G[vpai]:
                if pc[vadj] > pc[vpai] + G[vpai][vadj]:
                    pc[vadj] =  pc[vpai] + G[vpai][vadj]
                    pai[vadj] = vpai
                    atualizacao = True
        if not(atualizacao):
            break
    
    return not(atualizacao), pai, pc

def floydWarshall(G):
    pc = {}
    pai = {}
    V = list(G.keys())
    for vo in V:
        for vd in V:
            if vo == vd:
                pai[vo, vd] = None
                pc[vo, vd] = 0
            elif not(vd in G[vo]):
                pai[vo, vd] = None
                pc[vo, vd] = float('inf')
            else:
                pai[vo, vd] = vo
                pc[vo, vd] = G[vo][vd]

    for vk in V:
        for vo in V:
            for vd in V:
                if pc[vo,vd] > pc[vo,vk] + pc[vk,vd]:
                    pc[vo,vd] =  pc[vo,vk] + pc[vk,vd]
                    pai[vo,vd] = pai[vk,vd]
                
    return sorted(pai.items()), sorted(pc.items())
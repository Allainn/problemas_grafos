def profundidade(G, vo, vd):
    fila = []
    estado = vo
    mark = [estado]
    caminho_aux={estado: 'inicio'}
    while(True):
        if estado == vd:
            k = estado
            caminho = []
            while(k != 'inicio'):
                caminho.insert(0,k)
                k = caminho_aux[k]
            return caminho
        else:
            aux = list(G[estado].keys())
            flag = False
            for v in aux:
                if v not in mark:
                    caminho_aux[v] = estado
                    mark.append(v)
                    fila.insert(0,v)

            if fila==[]:
                return 0

            estado=fila.pop(0)
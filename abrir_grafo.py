import csv
import collections
def open_graph(filename, dir=True, ponderado=True):
    G = {}
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            vo = row[0].strip()
            vd = row[1].strip()
            if not(vo in G):
                G[vo] = {}
            if not(vd in G):
                G[vd] = {}
            if ponderado:
                peso = int(row[2].strip())
            else:
                peso = 1
                
            G[vo][vd] = peso
            if not(dir):
                G[vd][vo] = peso
                
    return collections.OrderedDict(sorted(G.items(), key=lambda t: t[0]))
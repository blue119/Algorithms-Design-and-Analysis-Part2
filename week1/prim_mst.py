from pprint import pprint
from random import randint
from time import time

class prime_mst(object):
    def _file_to_G(self, fn):
        G = []
        with open(fn, 'r') as f:
            t = f.readline().split()
            number_of_nodes = int(t[0])
            number_of_edges = int(t[1])
            V = range(1, number_of_nodes)

            for line in f.readlines():
                u = int(line.split()[0])
                v = int(line.split()[1])
                w = int(line.split()[2])
                G.append((u, v, w))
        return [G, number_of_nodes]

    def __init__(self, graph_file):
        self.G, n_of_nodes = self._file_to_G(graph_file)

        self.V = range(1, n_of_nodes+1)
        rnd_node = randint(1, n_of_nodes)

        # 1. randomly choose a node
        self.X = [rnd_node] # visited node
        self.T = [] # u, v and edge weight 

    def find_min_weight(self):
        # find whold adjacency
        adj_edges = []
        for u in self.X:
            for edge in self.G:
                if u in edge[:2]:
                    if edge.index(u) == 0 and edge[1] in self.X: continue # visited node
                    if edge.index(u) == 1 and edge[0] in self.X: continue # visited node
                    adj_edges.append(edge)

        adj_edges.sort(key = lambda x: x[2])
        edge_with_min_weight = adj_edges.pop(0)
        adj_v = edge_with_min_weight[0]
        if adj_v in self.X: adj_v = edge_with_min_weight[1]
        return [edge_with_min_weight, adj_v]


    def compute(self):
        while True:
            if len(self.X) >= len(self.V): break

            mw, v = self.find_min_weight()
            self.G.remove(mw) # avoid to look into visited edge
            self.X.append(v)
            self.T.append(mw)

graph_file = ['prim_example1.txt', 'edges.txt']
for f in graph_file:
    t1 = time()
    mst = prime_mst(f)
    mst.compute()
    #  print mst.X
    #  print mst.T
    c = 0
    for i in mst.T: c+=i[2]
    print 'Computer %s MST and spend %f' % (f, time()-t1)
    print 'the overall cost of mst: %d' % (c)


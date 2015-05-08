import networkx as nx
import numpy.random as nr
import pylab
import math


no_of_nodes=0

g=nx.Graph()
edge_list = [(1,1,0)]
node_energies = [3000]

no_of_nodes=raw_input('Enter the number of nodes')
no_of_nodes=int(no_of_nodes)

for i in range(1,no_of_nodes):
    node_energies.append(30)
    for j in range(1,no_of_nodes):
        if(i == j):
            continue
        else:
            temp1 = nr.random_integers(10)
            temp2 = nr.random_integers(10)
            if(temp2 > temp1):
                edge_list = edge_list + [(i,j,temp1)]

def createGraph():
    global g
    for i in range(1,no_of_nodes):
        g.add_node(i)
    g.add_weighted_edges_from(edge_list)
    nx.draw(g)
    pylab.show()


createGraph()

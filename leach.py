#program to illustrate leach protocol working process
import os
import pylab
import networkx as nx
import time
import math
import sim_file_leach as sfl


g=nx.Graph()
path_length = 0
edges_list = [(1,2,3),(1,3,2),(2,4,1),(3,4,8),(4,5,1)]
node_energies = [-3000,300,300,300,300,300]
cluster_heads = {"cluster1" : 3,"cluster2" : 4,"cluster3" : 2}


def createGraph():
 global g
 g.add_node(1,area='cluster1')
 g.add_node(2,area='cluster3')
 g.add_node(3,area='cluster1')
 g.add_node(4,area='cluster2')
 g.add_node(5,area='cluster2')
 g.add_weighted_edges_from(edges_list)



def transmit():
 global g
 source_node = raw_input('Enter the source node')
 dest_node = raw_input('Enter the destination node')
 no_of_bits = raw_input('Enter the number of bits in the packet')
 no_of_bits = int(no_of_bits)
 source_node = int(source_node)
 dest_node = int(dest_node)
 belonging_clusters = nx.get_node_attributes(g,'area')
 source_cluster_name = belonging_clusters[source_node]
 dest_cluster_name = belonging_clusters[dest_node]
 weights = nx.get_edge_attributes(g,'weight')
 source_cluster_head = cluster_heads[source_cluster_name]
 dest_cluster_head = cluster_heads[dest_cluster_name]
 overall_path = []
 
 print 'source cluster head is :' , source_cluster_head
 print 'destination cluster head is :' , dest_cluster_head
 if "Node-energy-Cycles-leach.csv" in os.listdir('.'):
   os.system("rm Node-energy-Cycles-leach.csv")
 fl =open("Node-energy-Cycles-leach.csv","a")
 

 for path in nx.all_simple_paths(g, source=source_node, target=dest_node):
    print path
    if source_cluster_head in path and dest_cluster_head in path :
       overall_path = path
       print 'Breaking here'
       break
 for node in overall_path:
   print 'Node energies are : ' , node_energies
   for energy in node_energies[1:]:
     fl.write(str(energy)+",")
   fl.write("\n") 
   if node == source_node:
   	node_energies[node]=node_energies[node]-(10*no_of_bits+0.02*no_of_bits*math.pow(path_length,2))        
   elif node == dest_node:
        node_energies[node]=node_energies[node]-(10*no_of_bits)    
   else : 
        node_energies[node]=node_energies[node]-5
 fl.close()
 print node_energies
 print overall_path
 sfl.initialSituation(g,source_node,dest_node)
 sfl.transmission(overall_path,g,source_node,dest_node)


createGraph() 
transmit()


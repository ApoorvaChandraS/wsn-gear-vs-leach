import networkx as nx
import numpy.random as nr
import pylab
import math
import time

no_of_nodes=0
no_of_broken_pairs = 0
g=nx.Graph()
edge_list = [(1,1,0)]
node_energies = [3000]
path_length=0

no_of_nodes=raw_input('Enter the number of nodes')
no_of_nodes=int(no_of_nodes)

for i in range(1,no_of_nodes):
    node_energies.append(300)
    for j in range(1,no_of_nodes):
        if(i == j):
            continue
        else:
            temp1 = nr.random_integers(10)
            temp2 = nr.random_integers(10)
            temp3 = nr.random_integers(10)
            temp4 = nr.random_integers(10)
            if(temp2 > temp1 and temp1 > temp3):
                edge_list = edge_list + [(i,j,temp1)]




def computeHNiR(list_of_neighbours,destination_node,source):
 dest_centroid = destination_node
 all_paths = []
 all_costs = []
 weights=nx.get_edge_attributes(g,'weight')
 print 'weights list is : ', weights
 for neighbour in list_of_neighbours:
   for path in nx.all_simple_paths(g, source=neighbour, target=destination_node):
    l=path
    cost = 0 
    if source not in path:
     try:
   	for i in range(len(path)):
    	 if i != (len(path)-1):
       		cost = cost + weights[(path[i],path[i+1])]
     except Exception,e:
        cost = cost + weights[(path[i+1],path[i])]
    
     path_length = cost
     #print path, "Cost : " + str(cost) 
     cost = 0.65*cost + 0.35*5 #the equation 
     all_costs = all_costs + [cost] 
     all_paths = all_paths + [path]

 print 'All costs is : ', all_costs
 print 'All paths is : ',all_paths


 min_cost = min(all_costs)
 index = all_costs.index(min_cost)
 return all_paths[index]







def transmit(source_node,dest_centroid):
 global g, no_of_broken_pairs
 if node_energies[source_node] < 7 :
   no_of_broken_pairs = no_of_broken_pairs + len(g.neighbors(source_node))
   g.remove_node(source_node)
   return
 #source_node=raw_input("Enter the source node : ")
 #destination_area=raw_input("Enter the destination node : ")
 #dest_centroid = int(destination_area)
 #source_node = int(source_node)
 neighbours_list = g.neighbors(source_node)
 print 'Neighbours list  is : ', neighbours_list
 if dest_centroid in neighbours_list: # trasmitting to a neighbour :
   mincost_path = [dest_centroid]
 else :  
  mincost_path=computeHNiR(neighbours_list,dest_centroid,source_node)
 print mincost_path
 #checking if all the nodes are alive on the path :
 for node in mincost_path :
   if node_energies[node] > 7:
     break
   else :
      print 'Node being removed is :' , node
      #time.sleep(4)       
      #no_of_broken_pairs = no_of_broken_pairs + len(g.neighbors(node))
      #g.remove_node(node)
 
 overall_path=[source_node] + mincost_path
 no_of_bits = 16
 for node in overall_path:
   if node == source_node:
   	node_energies[node]=node_energies[node]-(10*no_of_bits+0.02*no_of_bits*math.pow(path_length,2))
   elif node == dest_centroid:
        node_energies[node]=node_energies[node]-(10*no_of_bits)    
   else : 
        node_energies[node]=node_energies[node]-5

 print 'Packet transmitted through path : ', overall_path
 print 'Energies after transmission :' , node_energies[1:]


def checkAliveNodes():
 global g,node_energies,no_of_broken_pairs
 no_of_dead_nodes = 0
 index=0
 for energy in node_energies :
    if energy < 7 :
       index = node_energies.index(energy)
       no_of_dead_nodes = no_of_dead_nodes + 1 
       no_of_broken_pairs = no_of_broken_pairs + len(g.neighbors(index)) 
       #g.remove_node(index) 
 return no_of_dead_nodes     




def randomiseTransmissions():
 global g,no_of_broken_pairs
 num_of_packets = 18
 source_node = 0
 dest_node = 4000 
 k=0
 for i in range(1,num_of_packets):
    while True :
      source_node = nr.random_integers(no_of_nodes)
      dest_node = nr.random_integers(no_of_nodes) 
      if (source_node in g.nodes() and dest_node != source_node) and dest_node in g.nodes():
          break
      
    transmit(source_node,dest_node)  
    k=checkAliveNodes()
    if k >= no_of_nodes/2 :
       break
 print 'Half life : ' , str(i)
        
 print 'No of broken pairs after 20 transmissions : ' , no_of_broken_pairs


def check():
 global g
 for node in g.nodes():
   if len(g.neighbors(node))==0:
      g.remove_node(node)
   



def createGraph():
    global g
    for i in range(1,no_of_nodes):
        g.add_node(i)
    g.add_weighted_edges_from(edge_list)
    check()
    nx.draw(g)
    pylab.show()


createGraph()
randomiseTransmissions()

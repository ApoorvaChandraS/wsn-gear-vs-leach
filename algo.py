import pylab
import networkx as nx
import math
import os
import simulate_file as sf

g=nx.Graph()
path_length = 0

edges_list = [(1,2,3),(1,3,2),(2,4,1),(3,4,8),(4,5,1)]
node_energies = [-3000,300,300,300,300,300]
centroid_array = [('Koramangala',1),('BTM',2),('Indiranagar',3),('Rajajinagar',4),('Shivajinagar',5)]
energy_cycles = []

def createGraph(): #area specified for each node,weights or distances given for each edge
 global g
 g.add_node(1,area='Kor')
 g.add_node(2,area='BTM')
 g.add_node(3,area='Indiranagar')
 g.add_node(4,area='Rajajinagar')
 g.add_node(5,area='Shivajinagar')
 g.add_weighted_edges_from(edges_list)
 #nx.draw(g)
 #pylab.show()


def return_centroid(destination_area): #return the centroid for the requested region
 global g
 for (x,y) in centroid_array:
   if destination_area == x:
     print 'Centroid returned' , y
     return y  
 



def computeHNiR(list_of_neighbours,destination_area,source):
 dest_centroid = return_centroid(destination_area)
 all_paths = []
 all_costs = []
 weights=nx.get_edge_attributes(g,'weight')
 print 'weights list is : ', weights
 for neighbour in list_of_neighbours:
   for path in nx.all_simple_paths(g, source=neighbour, target=dest_centroid):
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
     print path, "Cost : " + str(cost) 
     cost = 0.65*cost + 0.35*5 #the equation 
     all_costs = all_costs + [cost] 
     all_paths = all_paths + [path]

 print 'All costs is : ', all_costs
 print 'All paths is : ',all_paths


 min_cost = min(all_costs)
 index = all_costs.index(min_cost)
 return all_paths[index]
     


def transmit():
 global g
 global energy_cycles
 source_node=raw_input("Enter the source node : ")
 destination_area=raw_input("Enter the destination area : ")
 no_of_bits = raw_input('Enter the number of bits in the packet')
 no_of_bits = int(no_of_bits)
 dest_centroid = return_centroid(destination_area)
 source_node = int(source_node)
 neighbours_list = g.neighbors(source_node)
 print 'Neighbours list  is : ', neighbours_list
 if dest_centroid in neighbours_list: # trasmitting to a neighbour :
   mincost_path = [dest_centroid]
 else :  
  mincost_path=computeHNiR(neighbours_list,destination_area,source_node)
 print mincost_path
 #checking if all the nodes are alive on the path :
 for node in mincost_path :
   if node_energies[node] > 7:
     break
   else :
      g.remove_node(node)
 
 overall_path=[source_node] + mincost_path
 if "Node-energy-cycles.csv" in os.listdir('.') :
    os.system("rm Node-energy-cycles.csv")
 
 fl = open("Node-energy-cycles.csv","a")

 for node in overall_path:
   print 'Node energies are : ' , node_energies
   for energy in node_energies[1:] :
     fl.write(str(energy)+",")
   fl.write("\n")
   if node == source_node:
   	node_energies[node]=node_energies[node]-(10*no_of_bits+0.02*no_of_bits*math.pow(path_length,2))        
   elif node == dest_centroid:
        node_energies[node]=node_energies[node]-(10*no_of_bits)    
   else : 
        node_energies[node]=node_energies[node]-5
   

 fl.close()
 print 'Packet transmitted through path : ', overall_path
 print 'Energies after transmission :' , node_energies[1:]
 #print 'Energy cycles are : ' ,energy_cycles
 sf.initialSituation(g,source_node,dest_centroid)
 sf.transmission(overall_path,g,source_node,dest_centroid)



createGraph()
 
transmit()
os.system("python LEACH/leach.py")

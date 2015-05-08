import os
import pylab
import networkx as nx

g=nx.Graph()

def drawGraph():
 global g;
 nx.draw(g,pos=nx.spectral_layout(g),nodecolor='b',edge_color = 'g')
 pylab.show()

def makeGraph():
 global g;
 g.add_node(1,area='CMH',energy=23);
 g.add_node(2,area='CMH');
 g.add_node(3,area='CMH');
 g.add_node(4,area='Kor');
 g.add_node(5,area='Kor');
 g.add_node(6,area='Kor');
 l=[(1,2,12),(2,3,5),(1,3,7),(4,5,10),(5,6,3),(4,6,12),(2,5,18),(2,4,5)]
 g.add_weighted_edges_from(l)




def packetStructure():
 global g
 areas=nx.get_node_attributes(g,'area') 
 print type(areas)
 source = object()
 destination = object()
 source=raw_input('Enter the source');
 destination=raw_input('Enter the destination')
 source_nodes = []
 target_nodes = []
 for x,y in areas.items(): #iterating through a dictionary
  if y == source:
   source_nodes = source_nodes + [x]
  if y == destination :
   target_nodes = target_nodes + [x]
 print 'Source nodes are : ' , source_nodes
 print 'Target nodes are : ' , target_nodes
 print 'The following are the source to destination paths : '
 for s_node in source_nodes :
  print '\n\n\n Paths from node : ' , s_node , '\n'
  for d_node in target_nodes:
    getPaths(s_node,d_node)
   



def queryRegion():
 global g
 areas=nx.get_node_attributes(g,'area')
 print list(set(areas.values()))
 #print areas[('Kor')]

def getPaths(src,tgt):
 global g
 weights=nx.get_edge_attributes(g,'weight')
 l=[]
 cost = 0
 #print(nx.dijkstra_path(g,1,5))
 for path in nx.all_simple_paths(g, source=src, target=tgt):
  l=path
  cost = 0 
  try:
   for i in range(len(path)):
     if i != (len(path)-1):
       cost = cost + weights[(path[i],path[i+1])]
  except Exception,e:
       cost = cost + weights[(path[i+1],path[i])]
    
  print path, "Cost : " + str(cost)

 

makeGraph()
drawGraph()
#getPaths()
queryRegion()
packetStructure()

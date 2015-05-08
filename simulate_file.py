import os
import networkx as nx
import pylab
import math
import time
import numpy 
node_colors = []
edge_colors = []
bar_colors = []
node_positions = [(0.0,0.0),(0.5,1),(0.6,1.1),(0.0,0.9),(0.0,0.1),(0.65,0.0)]
disp_count = 0

def initialize_edge_colors(i):
 for j in range(len(edge_colors)) :
    if i == j :
       edge_colors[j] = 'r'
    else :
       edge_colors[j] = 'k'


def initializeEnergies(line_number) :
  fl = open("Node-energy-cycles.csv","r")
  ec = []
  c=0
  for line in fl :
     ec = line.split(",")
     c=c+1
     if  c == line_number :
        break
  ec =  ec[:-1] 
  x=[]
  for y in ec :
    x=x+[float(y)]
  initializeBarColours(line_number,len(x))
  return x 
   
     
 

def transmission(path,g,src,dest):
 global disp_count
 k=0
 j=0
 list_of_edges = g.edges() 
 for node in path :
  k=path.index(node)
  disp_count = disp_count + 1
  if k != (len(path)-1):
   k=path[k+1]
   j=list_of_edges.index((node,k))
   initialize_edge_colors(j)
   #ec[disp_count].remove(-3000) 
   pylab.subplot(121) 
   nx.draw_networkx(g,pos = nx.circular_layout(g),node_color= node_colors,edge_color = edge_colors)
   pylab.annotate("Source",node_positions[src])
   pylab.annotate("Destination",node_positions[dest])
   pylab.title("Transmission")

   pylab.subplot(122)
   pylab.bar(left=[1,2,3,4,5],height=[300,300,300,300,300],width=0.5,color = ['w','w','w','w','w'],linewidth=0) 
   pylab.bar(left=[1,2,3,4,5],height=initializeEnergies(disp_count),width=0.5,color = bar_colors) 
   pylab.title("Node energies")
   #pylab.legend(["already passed throgh","passing" , "yet to pass"])
   pylab.xlabel('Node number')
   pylab.ylabel('Energy') 
   pylab.suptitle('GEAR Protocol', fontsize=12) 
   pylab.pause(2)
  else :
     return



def initializeBarColours(lineNumber,noOfNodes):
  global bar_colors 
  for i in range(noOfNodes) :
     if i < lineNumber :
        bar_colors[i] = 'g'
     elif i == lineNumber :
        bar_colors[i] = 'r'
     else :
        bar_colors[i] = 'b' 
 
 
 

def initialSituation(g,src,dest):
 global node_colors
 global edge_colors
 global disp_count
 global bar_colors
 #print ec
 dest_location = len(g.nodes())-1 
 for node in g.nodes():
  if node == src :
    node_colors = node_colors + ['b']
  elif node == dest :
    node_colors = node_colors + ['y']  
  else :
    node_colors = node_colors + ['r']  
  edge_colors = edge_colors + ['k']
  bar_colors = bar_colors + ['b']

 #ec[disp_count].remove(-3000)
 disp_count = disp_count + 1
 print 'Initialize energies :' , initializeEnergies(disp_count)
 pylab.subplot(121) 
 
 nx.draw_networkx(g,pos = nx.circular_layout(g),node_color= node_colors,edge_color = edge_colors)
 pylab.annotate("Source",node_positions[src])
 pylab.annotate("Destination",node_positions[dest])
 pylab.title("Before Transmission")

 pylab.subplot(122)
 pylab.bar(left=[1,2,3,4,5],height=[300,300,300,300,300],width=0.5,color = ['w','w','w','w','w'],linewidth=0) 
 pylab.bar(left=[1,2,3,4,5],height=initializeEnergies(disp_count),width=0.5,color = bar_colors) 
 #pylab.legend(["already passed throgh","passing" , "yet to pass"])
 pylab.title("Node energies")
 pylab.xlabel('Node number')
 pylab.ylabel('Energy')
 pylab.suptitle('GEAR Protocol', fontsize=12) 
 pylab.pause(2)
 
 
 


def simulate(g):
 initialSituation(g)
 transmission([1,2,4,5],g)


#simulate(g)

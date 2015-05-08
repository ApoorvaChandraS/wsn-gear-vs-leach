import pylab

x=[11,12,13,14,15,16,17,18,19]
y=[7,8,9,10,10,11,12,13,13]

pylab.bar(x,y)
pylab.xlabel('Network size - number of nodes')
pylab.ylabel('Number of packets transmitted by half life')
pylab.title('Network life - GEAR only')
pylab.show()  

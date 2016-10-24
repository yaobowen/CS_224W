'''
This script is for hw2 question3
'''

from snap import *
import random
import numpy as np
import matplotlib.pyplot as plt

#/---------------------q3.1------------------/
def decisionProcess(G):
	flag=1
	nodesId=range(10000)
	for it in xrange(10):
		for nId in nodesId:
			n=G.GetNI(nId)
			if(G.GetIntAttrDatN(n,'strong')==0):
				cA=0
				cB=0
				d=n.GetDeg()
				for k in xrange(d):
					neighbor=n.GetNbrNId(k)
					vote=G.GetIntAttrDatN(neighbor,'vote')
					if(vote==1):
						cA+=1
					elif(vote==-1):
						cB+=1
				if(cA>cB):
					G.AddIntAttrDatN(n,1,'vote')
				elif(cB>cA):
					G.AddIntAttrDatN(n,-1,'vote')
				else:
					G.AddIntAttrDatN(n,flag,'vote')
					flag=-flag	

def constructGraph(G):
	G.AddIntAttrN('vote')
	G.AddIntAttrN('strong')
	for n in G.Nodes():
		nId=n.GetId()
		if(nId%10<=3):
			G.AddIntAttrDatN(n,1,'vote')
			G.AddIntAttrDatN(n,1,'strong')
		elif(nId%10>=8):
			G.AddIntAttrDatN(n,0,'vote')
			G.AddIntAttrDatN(n,0,'strong')
		else:
			G.AddIntAttrDatN(n,-1,'vote')
			G.AddIntAttrDatN(n,1,'strong')	

def countVote(G,toprint=True):
	cA=0
	cB=0
	for n in G.Nodes():
		vote=G.GetIntAttrDatN(n,'vote')
		if(vote==1):
			cA+=1
		elif(vote==-1):
			cB+=1
		else:
			print 'badbad'
	if(toprint):
		print 'number of votes for A: '+str(cA)
		print 'number of votes for B: '+str(cB)
		print 'A win by B: '+str(cA-cB)
	return cA-cB

#consruct the graph
g1=LoadEdgeList(PNEANet,'graph1.txt',0,1)
g2=LoadEdgeList(PNEANet,'graph2.txt',0,1)
constructGraph(g1)
constructGraph(g2)
decisionProcess(g1)
decisionProcess(g2)
print 'result for graph1:'
countVote(g1)
print 'result for graph2:'
countVote(g2)



#/---------------------q3.2------------------/
g1win=[]
g2win=[]
ks=range(1000,10000,1000)
for k in ks:
	affected=range(3000,3000+k/100)
	g1=LoadEdgeList(PNEANet,'graph1.txt',0,1)
	g2=LoadEdgeList(PNEANet,'graph2.txt',0,1)
	constructGraph(g1)
	constructGraph(g2)
	for nid in affected:
		g1.AddIntAttrDatN(nid,1,'vote')
		g1.AddIntAttrDatN(nid,1,'strong')
		g2.AddIntAttrDatN(nid,1,'vote')
		g2.AddIntAttrDatN(nid,1,'strong')
	decisionProcess(g1)
	decisionProcess(g2)
	g1win.append(countVote(g1,False))
	g2win.append(countVote(g2,False))

print g1win
print g2win
plt.figure(1)
plt.plot(ks,g1win,'b-',ks,g2win,'r-')
plt.xlabel('Value of K')
plt.ylabel('Candidate A win by')
plt.legend(['Graph 1','Graph 2']);
plt.title('Effect of Advertising');
plt.savefig('Effect_of_Advertising.png');


#/---------------------q3.3------------------/
#get the degree rank
g1=LoadEdgeList(PNEANet,'graph1.txt',0,1)
g2=LoadEdgeList(PNEANet,'graph2.txt',0,1)
constructGraph(g1)
constructGraph(g2)
dic_deg1={}
dic_deg2={}
for n in g1.Nodes():
	dic_deg1[n.GetId()]=n.GetDeg()
for n in g2.Nodes():
	dic_deg2[n.GetId()]=n.GetDeg()
vec_deg1=sorted(dic_deg1,key=lambda x:(-dic_deg1[x],x))
vec_deg2=sorted(dic_deg2,key=lambda x:(-dic_deg2[x],x))

#begin analyse
g1win=[]
g2win=[]
ks=range(1000,10000,1000)

for k in ks:
	g1=LoadEdgeList(PNEANet,'graph1.txt',0,1)
	g2=LoadEdgeList(PNEANet,'graph2.txt',0,1)
	constructGraph(g1)
	constructGraph(g2)
	affected1=vec_deg1[:k/1000]
	affected2=vec_deg2[:k/1000]
	for nid in affected1:
		print dic_deg1[nid]
		g1.AddIntAttrDatN(nid,1,'vote')
		g1.AddIntAttrDatN(nid,1,'strong')
	print '--------------'
	for nid in affected2:
		print dic_deg2[nid]
		g2.AddIntAttrDatN(nid,1,'vote')
		g2.AddIntAttrDatN(nid,1,'strong')
	decisionProcess(g1)
	decisionProcess(g2)
	g1win.append(countVote(g1,False))
	g2win.append(countVote(g2,False))

print g1win
print g2win
plt.figure(2)
plt.plot(ks,g1win,'b-',ks,g2win,'r-')
plt.xlabel('Value of K')
plt.ylabel('Candidate A win by')
plt.legend(['Graph 1','Graph 2']);
plt.title('Effect of Affecting High Rollers');
plt.savefig('Effect_of_Affecting_High_Rollers.png');

# #/---------------------q3.4------------------/
g1=LoadEdgeList(PNEANet,'graph1.txt',0,1)
g2=LoadEdgeList(PNEANet,'graph2.txt',0,1)
deg_count1={}
deg_count2={}
d=0
for n in g1.Nodes():
	d = n.GetDeg()
	if(d in deg_count1):
		deg_count1[d] += 1
	else:
		deg_count1[d] = 1
for n in g2.Nodes():
	d = n.GetDeg()
	if(d in deg_count2):
		deg_count2[d] += 1
	else:
		deg_count2[d] = 1
values1=1.0*np.array(deg_count1.values())/np.sum(np.array(deg_count1.values()))
values2=1.0*np.array(deg_count2.values())/np.sum(np.array(deg_count2.values()))
plt.figure(3)
plt.plot(deg_count1.keys(), values1, 'b.',deg_count2.keys(), values2, 'r.')
plt.xlabel('log degree')
plt.ylabel('log probability')
plt.xscale('log')
plt.yscale('log')
plt.title('Log-Log Degree Distribution')
plt.legend(['Graph1', 'Graph2'])
plt.savefig('Log-Log_Degree Distribution.png')


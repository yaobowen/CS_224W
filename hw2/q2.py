'''
This script is for hw2 question2
'''

from snap import *
import random
import numpy as np
import matplotlib.pyplot as plt

G=LoadEdgeList(PNEANet,'epinions-signed.txt',0,1)
G.AddIntAttrE('sign')
f=open('epinions-signed.txt')
c=0
for l in f:
	data=l.split('\t')
	src=int(data[0])
	dst=int(data[1])
	sign=int(data[2])
	e=G.GetEI(src, dst)
	G.AddIntAttrDatE(e, sign, 'sign')
	c+=1

for e in G.Edges():
	if (e.GetSrcNId()==e.GetDstNId()):
		G.DelEdge(e.GetSrcNId(), e.GetDstNId())
print 'Finish Loading Data'
print G.GetNodes()


#/---------------------q2.1-a------------------/
c=0
list_o_count=[0]*4
for e in G.Edges():
	c+=1
	if(c%1000==0):
		print c
	n1=e.GetSrcNId()
	n2=e.GetDstNId()
	n1I=G.GetNI(n1)
	n2I=G.GetNI(n2)
	n1deg=n1I.GetDeg()
	for i in xrange(n1deg):
		nid=n1I.GetNbrNId(i)
		if(n2I.IsNbrNId(nid)):#is a common neighbor
			posi_count=0

			#for n1 and the common neighbor
			if(G.IsEdge(n1,nid)):
				ed=G.GetEI(n1,nid)
			else:
				ed=G.GetEI(nid,n1)
			if(G.GetIntAttrDatE(ed,'sign')>0):
				posi_count+=1

			#for n2 and the common neighbor
			if(G.IsEdge(n2,nid)):
				ed=G.GetEI(n2,nid)
			else:
				ed=G.GetEI(nid,n2)
			if(G.GetIntAttrDatE(ed,'sign')>0):
				posi_count+=1

			#for n1 and n2
			if(G.GetIntAttrDatE(e,'sign')>0):
				posi_count+=1

			#add the number of the corresponding triad
			list_o_count[posi_count]+=1

			
myarray=np.array(list_o_count)
print myarray
print myarray/3.0
print 1.0*myarray/np.sum(myarray)

#/---------------------q2.1-b-------------------/
count=0
for e in G.Edges():
	if(G.GetIntAttrDatE(e,'sign')>0):
		count+=1
print 'the fraction of positive edge is:'
print count*1.0/G.GetEdges()


#/---------------------q2.4-b-------------------/
def isBalance(G):
	left=[]
	right=[]
	for n in G.Nodes():
		inleft=True
		inright=True
		for nodeId in left:
			p=min(n.GetId(),nodeId)
			q=max(n.GetId(),nodeId)
			e=G.GetEI(p,q)
			if(G.GetIntAttrDatE(e,'sign')<0):
				inleft=False
			if(G.GetIntAttrDatE(e,'sign')>0):
				inright=False
		if((not inleft) and (not inright)):
			return False
		for nodeId in right:
			p=min(n.GetId(),nodeId)
			q=max(n.GetId(),nodeId)
			e=G.GetEI(p,q)
			if(G.GetIntAttrDatE(e,'sign')<0):
				inright=False
			if(G.GetIntAttrDatE(e,'sign')>0):
				inleft=False
		if((not inleft) and (not inright)):
			return False
		if(inleft):
			left.append(n.GetId())
		else:
			right.append(n.GetId())	
	return True



random.seed()
num_o_iter=0
num_o_balanced=0
while(num_o_iter<100):
	num_o_iter+=1

	#construct the graph
	cG=TNEANet.New()
	cG.AddIntAttrE('sign')
	for i in xrange(10):
		cG.AddNode(i)
	for i in xrange(9):
		for j in xrange(i+1,10):
			cG.AddEdge(i,j)
	for e in cG.Edges():
		if(random.random()>0.5):
			cG.AddIntAttrDatE(e,1,'sign')
		else:
			cG.AddIntAttrDatE(e,-1,'sign')

	#begin dynamic process
	count=0
	nodes=range(10)
	while(count<1000000):
		count+=1

		#check if it is balance every 1000 iterations
		if(count%1000==0):
			if(isBalance(cG)):
				break

		#randomly pick a triad and test if it's balanced
		sample=random.sample(nodes,3)
		sample.sort()
		num_o_posi=0
		e1=cG.GetEI(sample[0],sample[1])
		e2=cG.GetEI(sample[0],sample[2])
		e3=cG.GetEI(sample[1],sample[2])
		if(cG.GetIntAttrDatE(e1,'sign')>0):
			num_o_posi+=1
		if(cG.GetIntAttrDatE(e2,'sign')>0):
			num_o_posi+=1
		if(cG.GetIntAttrDatE(e3,'sign')>0):
			num_o_posi+=1

		#if the triad is unbalanced, then randomly choose one edge and flip it
		if(num_o_posi==0 or num_o_posi==2):
			r=random.random()
			if(r<1.0/3):
				si=cG.GetIntAttrDatE(e1,'sign')
				cG.AddIntAttrDatE(e1,-si,'sign')
			elif(r>2.0/3):
				si=cG.GetIntAttrDatE(e3,'sign')
				cG.AddIntAttrDatE(e3,-si,'sign')
			else:
				si=cG.GetIntAttrDatE(e2,'sign')
				cG.AddIntAttrDatE(e2,-si,'sign')
	if(isBalance(cG)):
		num_o_balanced+=1
print num_o_balanced



















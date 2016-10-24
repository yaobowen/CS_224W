'''
This script generates a simple sample graph
'''
from snap import *
import random

# def isBalance(G):
# 	left=[]
# 	right=[]
# 	for n in G.Nodes():
# 		inleft=True
# 		inright=True
# 		for nodeId in left:
# 			p=min(n.GetId(),nodeId)
# 			q=max(n.GetId(),nodeId)
# 			e=G.GetEI(p,q)
# 			if(G.GetIntAttrDatE(e,'sign')<0):
# 				inleft=False
# 			if(G.GetIntAttrDatE(e,'sign')>0):
# 				inright=False
# 		if((not inleft) and (not inright)):
# 			return False
# 		for nodeId in right:
# 			p=min(n.GetId(),nodeId)
# 			q=max(n.GetId(),nodeId)
# 			e=G.GetEI(p,q)
# 			if(G.GetIntAttrDatE(e,'sign')<0):
# 				inright=False
# 			if(G.GetIntAttrDatE(e,'sign')>0):
# 				inleft=False
# 		if((not inleft) and (not inright)):
# 			return False
# 		if(inleft):
# 			left.append(n.GetId())
# 		else:
# 			right.append(n.GetId())	
# 	return True

# g=TNEANet.New();
# g.AddIntAttrE('sign')
# for i in xrange(10):
# 	g.AddNode(i)
# for i in xrange(9):
# 	for j in xrange(i+1,10):
# 		g.AddEdge(i,j)
# left=random.sample(range(10),4)
# right=[item for item in range(10) if item not in left]
# left.sort()
# right.sort()
# print left
# print right
# for i in xrange(len(left)-1):
# 	for j in xrange(i+1,len(left)):
# 		e=g.GetEI(left[i],left[j])
# 		g.AddIntAttrDatE(e,1,'sign')
# for i in xrange(len(right)-1):
# 	for j in xrange(i+1,len(right)):
# 		e=g.GetEI(right[i],right[j])
# 		g.AddIntAttrDatE(e,1,'sign')
# for i in left:
# 	for j in right:
# 		p=min(i,j)
# 		q=max(i,j)
# 		e=g.GetEI(p,q)
# 		g.AddIntAttrDatE(e,-1,'sign')
# p=min(left[3],right[5])
# q=max(left[3],right[5])
# e=g.GetEI(p,q)
# g.AddIntAttrDatE(e,1,'sign')
# print isBalance(g)


g=TNEANet.New();
g.AddIntAttrE('sign')
g.AddNode(1);
g.AddNode(2);
g.AddNode(10);
g.AddNode(3);
g.AddNode(6);
g.AddNode(4);
for n in g.Nodes():
	print n.GetId();
g.AddEdge(1,2);
g.AddEdge(1,3);
g.AddEdge(1,4);
g.AddEdge(2,3);
g.AddEdge(2,4);
g.AddEdge(3,4);
e=g.GetEI(1,2);
g.AddIntAttrDatE(e,1,'sign')
e=g.GetEI(1,3);
g.AddIntAttrDatE(e,1,'sign')
e=g.GetEI(2,3);
g.AddIntAttrDatE(e,1,'sign')
e=g.GetEI(1,4);
g.AddIntAttrDatE(e,-1,'sign')
e=g.GetEI(2,4);
g.AddIntAttrDatE(e,-1,'sign')
e=g.GetEI(3,4);
g.AddIntAttrDatE(e,-1,'sign')












'''
This script is for hw1-q3
'''

from snap import *
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def h(u,v):
	re=1
	while(u/2 != v/2):
		re+=1
		u/=2
		v/=2
	return re

def addedge(G,v,k,alpha):
	random.seed(1)
	i=0
	r=0
	n=G.GetNodes()
	Z=0
	for u in xrange(1,n+1):
		if(u!=v):
			Z+=2**(-alpha*h(v,u))
	neighbors=[v]
	while(i<k):
		r=random.uniform(0.0,Z)
		temp=0
		for u in xrange(1,n+1):
			if(u not in neighbors):
				temp+=2**(-alpha*h(v,u))
				if(temp>=r):
					G.AddEdge(v,u)
					neighbors.append(u)
					i+=1
					Z-=2**(-alpha*h(v,u))
					break
	return


alpha_list=range(1,101)
for i in xrange(len(alpha_list)):
	alpha_list[i]/=10.0
print alpha_list

avg_path_len_list=[]
suc_prob_list=[]

for alpha in alpha_list:
	print 'Now processing alpha = '+str(alpha)
	#Iniytialize the graph
	G=TNGraph.New()
	for i in xrange(1,2**10+1):
		G.AddNode(i)
	for i in xrange(1,2**10+1):
		addedge(G,i,5,alpha)
	#Other initialization
	path_len_list=[]
	suc=0

	#Sample 1000 edges
	random.seed(1)
	big=[]
	c=0
	for i in xrange(1,1024+1):
		for j in xrange(1,1024+1):
			if(i!=j):
				big.append([i,j])
	sample=random.sample(big,  1000)
	
	#Begin search for each pair
	for pair in sample:
		s=pair[0]
		t=pair[1]
		path=1
		while(True):
			sn=G.GetNI(s)
			u=sn.GetOutNId(0)
			for i in xrange(1,5):
				n=sn.GetOutNId(i)
				if(h(n,t)<h(u,t)):
					u=n
			if(u==t):
				path_len_list.append(path)
				suc+=1
				break
			elif(h(u,t)<h(s,t)):
				s=u
				path+=1
			else:
				break

	avg_path_len_list.append(np.mean(np.array(path_len_list)))
	suc_prob_list.append((suc*1.0)/1000)

print avg_path_len_list
print suc_prob_list

plt.figure(1);
plt.plot(alpha_list,avg_path_len_list,'b-');
plt.xlabel('Alpha');
plt.ylabel('Average searching length');
plt.title('Average searching length V.S. Alpha');
plt.savefig('Average searching length V.S. Alpha.png');

plt.figure(2);
plt.plot(alpha_list,suc_prob_list,'r-');
plt.xlabel('Alpha');
plt.ylabel('Search success probability');
plt.title('Search success probability V.S. Alpha');
plt.savefig('Search success probability V.S. Alpha.png');



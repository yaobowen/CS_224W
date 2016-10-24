'''
This script is for hw1-q1
'''

from snap import * 
import random
import matplotlib.pyplot as plt
import numpy as np;

#Some functions for this problem set
def getExDeg(G,p,z):
	for i in xrange(len(z)):
		d=p[i];
		for n in G.Nodes():
			for j in xrange(n.GetDeg()):
				if( (G.GetNI(n.GetNbrNId(j)).GetDeg()) ==d+1):
					z[i]=z[i]+1;
	s=sum(z);
	for i in xrange(len(z)):
		z[i]=z[i]/(1.0*s);	

def calEpDeg(x,y):
	ss=0;
	for i in xrange(len(x)):
		ss+=x[i]*y[i];
	return ss;

def getClCoef(G,N):
	d=N.GetDeg();
	if(d<=1):
		return 0;
	e=0;
	for i in xrange(d):
		p=N.GetNbrNId(i);
		for j in xrange(i+1,d):
			if(G.IsEdge(p,N.GetNbrNId(j))):
				e+=1;
	return (2.0*e)/(d*(d-1));


#/------------------------------------/#
#q1-1
random.seed(1);
#Generate the Erdos-Renyi random graph
ER=GenRndGnm(PUNGraph,5242,14484,False);

#Generate the small world graph
SW=TUNGraph.New();
for i in xrange(5242):
	SW.AddNode(i);

for i in xrange(0,5241):
	SW.AddEdge(i,i+1);
SW.AddEdge(5241,0);

for i in xrange(5240):
	SW.AddEdge(i,i+2);
SW.AddEdge(5240,0);
SW.AddEdge(5241,1);

c=0;
sample=range(5242)
while(True):
	if(c>=4000):
		break;
	else:
		l=random.sample(sample,2);
		if(not SW.IsEdge(l[0],l[1])):
			SW.AddEdge(l[0],l[1]);
			c=c+1;


#Load in the Real-World network
RW=LoadEdgeList(PUNGraph,"ca-GrQc.txt",0,1);
for e in RW.Edges():
	if (e.GetSrcNId()==e.GetDstNId()):
		RW.DelEdge(e.GetSrcNId(),e.GetDstNId());

#Prepare data for plotting
c1=TIntPrV();
c2=TIntPrV();
c3=TIntPrV();
GetDegCnt(ER,c1);
GetDegCnt(SW,c2);
GetDegCnt(RW,c3);
x1=[];x2=[];x3=[];
y1=[];y2=[];y3=[];
for i in c1:
	x1.append(i.GetVal1());
	y1.append(i.GetVal2()/5242.0);
for i in c2:
	x2.append(i.GetVal1());
	y2.append(i.GetVal2()/5242.0);
for i in c3:
	x3.append(i.GetVal1());
	y3.append(i.GetVal2()/5242.0);

#Plot
# plt.figure(1);
# plt.plot(x1,y1,'r-',x2,y2,'g-',x3,y3,'b-');
# plt.xscale('log');
# plt.yscale('log');
# plt.xlabel('Degree');
# plt.ylabel('Probability');
# plt.title('Degree Distribution');
# plt.legend(['Erdos-Renyi','Small World','Real World']);
# plt.savefig('DegDist.png');

#/--------------------------------/#
#q1-2-a
#Prepare the data
z1=[0]*len(x1);
z2=[0]*len(x2);
z3=[0]*len(x3);
p1=np.array(x1)-1;
p2=np.array(x2)-1;
p3=np.array(x3)-1;


getExDeg(ER,p1,z1);
getExDeg(SW,p2,z2);
getExDeg(RW,p3,z3);

#Plot
# plt.figure(2);
# plt.plot(p1,z1,'r-',p2,z2,'g-',p3,z3,'b-');
# plt.xscale('log');
# plt.yscale('log');
# plt.xlabel('Excess Degree');
# plt.ylabel('Probability');
# plt.title('Excess Degree Distribution');
# plt.legend(['Erdos-Renyi','Small World','Real World']);
# plt.savefig('ExDegDist.png');

#Calculate the expected degree and expected excess degree
ed=[0]*3;
esd=[0]*3;

ed[0]=calEpDeg(x1,y1);
ed[1]=calEpDeg(x2,y2);
ed[2]=calEpDeg(x3,y3);
esd[0]=calEpDeg(p1,z1);
esd[1]=calEpDeg(p2,z2);
esd[2]=calEpDeg(p3,z3);

print 'Expected Degree:';
for i in xrange(3):
	print ed[i];
print 'Expected Excess Degree:';
for i in xrange(3):
	print esd[i];

#Calculate Average Clustering Coefficient:
c=0;
for N in ER.Nodes():
	c+=getClCoef(ER,N);
c=1.0*c/ER.GetNodes();
print 'The Average Clustering Coefficient for Erdos-Renyi Network is:'
print c;

c=0;
for N in SW.Nodes():
	c+=getClCoef(SW,N);
c=1.0*c/SW.GetNodes();
print 'The Average Clustering Coefficient for Small World Network is:'
print c;

c=0;
for N in RW.Nodes():
	c+=getClCoef(RW,N);
c=1.0*c/RW.GetNodes();
print 'The Average Clustering Coefficient for Real World Network is:'
print c;



























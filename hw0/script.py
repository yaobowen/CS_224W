'''
This script is for hw0-q1
'''

import snap;

# g=snap.TUNGraph.New();
# g.AddNode(1);
# g.AddNode(2);
# g.AddNode(3);
# g.AddEdge(1,2);
# g.AddEdge(2,1);
# g.AddEdge(1,3);
# g.AddEdge(1,1);


g=snap.LoadEdgeList(snap.PNGraph,"wiki-Vote.txt",0,1)

print g.GetNodes();
print "\n";

c=0;
for e in g.Edges():
	if(e.GetSrcNId()==e.GetDstNId()):
		c=c+1;
print c;
print "\n"

# c=0;
# for e in g.Edges():
# 	if(e.GetSrcNId()!=e.GetDstNId()):
# 		c=c+1;
# print c;
# print "\n"
print snap.CntUniqDirEdges(g);
print '\n';


# cc=0;
# ug=snap.ConvertGraph(snap.PUNGraph,g);
# for e in ug.Edges():
# 	if(e.GetSrcNId()!=e.GetDstNId()):
# 		cc=cc+1;
# print cc;
# print "\n";
print snap.CntUniqUndirEdges(g);
print '\n';


# print c-cc;
# print "\n";
print snap.CntUniqBiDirEdges(g);
print '\n';

c=0;
for n in g.Nodes():
	if(n.GetOutDeg()==0):
		c=c+1;
print c;
print "\n";

c=0;
for n in g.Nodes():
	if(n.GetInDeg()==0):
		c=c+1;
print c;
print "\n";

c=0;
for n in g.Nodes():
	if(n.GetOutDeg()>10):
		c=c+1;
print c;
print "\n";

c=0;
for n in g.Nodes():
	if(n.GetInDeg()<10):
		c=c+1;
print c;
print "\n";

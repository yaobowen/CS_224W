'''
This script is for hw0-q2
'''

import snap;

g=snap.LoadEdgeList(snap.PNGraph,'wiki-Vote.txt',0,1);

wccgv=snap.TCnComV();
snap.GetWccs(g,wccgv);
print wccgv.Len();

wccg=snap.GetMxWcc(g);
print wccg.GetNodes();
print wccg.GetEdges();


PRankH=snap.TIntFltH();
snap.GetPageRank(g,PRankH);
PRankH.SortByDat(False);
a=0;
for item in PRankH:
	if(a<3):
		print item,PRankH[item];
		a=a+1;
	else:
		break;
print "\n";

HubH=snap.TIntFltH();
AutH=snap.TIntFltH();
snap.GetHits(g,HubH,AutH);
HubH.SortByDat(False);
AutH.SortByDat(False);
a=0;
for item in HubH:
	if(a<3):
		print item,HubH[item];
		a=a+1;
	else:
		break;
print "\n"

a=0;
for item in AutH:
	if(a<3):
		print item,AutH[item];
		a=a+1;
	else:
		break;









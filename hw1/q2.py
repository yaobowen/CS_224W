'''
This script is for hw1-q2
'''

from snap import * 
import matplotlib.pyplot as plt
import numpy as np;
import sqlite3 as sql;

connection=sql.connect("actor.db");
connection.text_factory=str;
cursor=connection.cursor();

G=LoadEdgeList(PUNGraph,"imdb_actor_edges.tsv",0,1);
LWCC=GetMxWcc(G);
DegCen={};
BetCenH=TIntFltH();
Dummy=TIntPrFltH();
BetCen={};
CloCen={};
for n in LWCC.Nodes():
	DegCen[n.GetId()]=GetDegreeCentr(LWCC,n.GetId());
	CloCen[n.GetId()]=GetClosenessCentr(LWCC,n.GetId());
GetBetweennessCentr(LWCC,BetCenH,Dummy);
print "Done";
for key in BetCenH:
	BetCen[key]=BetCenH[key];



format_str='update actor set DegCen={}, BetCen={}, CloCen={} where ID={};';
for i in DegCen.keys():
	q=format_str.format(DegCen[i],BetCen[i],CloCen[i],i);
	print q;
	cursor.execute(q);
connection.commit();
connection.close();

#/---------------------------------/#
#Print out the result
print "the top 20 DegCen:";
q='select name ,movies_95_04,DegCen from actor order by DegCen Desc limit 20';
cursor.execute(q);
result=cursor.fetchall();
for r in result:
	print r;
print "the average Deg:"
q='select avg(movies_95_04) from actor';
cursor.execute(q);
result=cursor.fetchall();
for r in result:
	print r;


print "the top 20 BetCen:";
q='select name,genres,BetCen from actor order by BetCen Desc limit 20';
cursor.execute(q);
result=cursor.fetchall();
for r in result:
	print r;

print "the top 20 CloCen:";
q='select name,genres,CloCen from actor order by CloCen Desc limit 20';
cursor.execute(q);
result=cursor.fetchall();
for r in result:
	print r;

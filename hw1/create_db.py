import sqlite3 as sql

connection=sql.connect("actor.db");
connection.text_factory =str;
cursor=connection.cursor();

data=[]
with open("imdb_actors_key.tsv",'r') as f:
	for lines in f:
		d=lines.split('\t');
		data.append(d);
data.pop(0);

sql_command="""
create table actor(
ID interger primary key,
name varchar(20), 
movies_95_04 interger,
main_genre varchar(20),
genres varchar(50),
DegCen float(10),
BetCen float(10),
CloCen float(10));
"""

cursor.execute(sql_command);


format_string='insert into actor(ID,name,movies_95_04,main_genre,genres) values ("{}",{},"{}","{}","{}");'
for l in data:
	sql_command=format_string.format(l[0],l[1],
		l[2],l[3],l[4]);
	cursor.execute(sql_command);

connection.commit();
connection.close();
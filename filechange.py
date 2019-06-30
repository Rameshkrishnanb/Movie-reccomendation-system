 # -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:29:54 2019

@author: Ramesh Krishnan B
"""

fr=open('F:\Project2\mllatestsmall/tags_large.csv')
fw=open('F:\Project2\mllatestsmall/tags_new.csv','w')
line=fr.readline()

heading='movieid,tags\n' 

movies={}
fw.writelines(heading)
count=0
for line in fr:
    col=line.split(',')
    
    movieid=col[1]
    tag=col[2]
    if movieid in movies.keys():
        movies[movieid]+=' '+tag
    else:
        movies[movieid]=tag
    if count==103000:
        break
    count+=1
    
for movieid in movies.keys():
    line=movieid+','+movies[movieid]+'\n'
    fw.writelines(line)
len(movies.keys())
fr.close()
fw.close()
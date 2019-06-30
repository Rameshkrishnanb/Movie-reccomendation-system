# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 12:46:52 2019

@author: Ramesh Krishnan B
"""

fr=open('ratings.csv','r')
movies={}
count=0
line=fr.readline()
print (line)
for line in fr:
    userid=line.split(',')[0]
    if userid in movies.keys():
        movies[userid]+=1
    else:
        movies[userid]=1
    count+=1
fr.close()

#print (movies)
print(str(count)+' lines scanned')
fr=open('ratings.csv')
fw=open('ratings_test.csv','w') #ratings_20.csv is the original file
fw.writelines(fr.readline())
count=0
for line in fr:
    userid=str(line.split(',')[0])
    #print (userid)
    #if count==100:
     #   break
    count+=1
    if (movies[userid]>=20):
        fw.writelines(line)
fr.close()
fw.close()
for userid in movies.keys():
    if movies[userid]==max(movies.values()):
        print (userid,' has given the highest number of ratings')
        
print(str(count)+' lines written')  

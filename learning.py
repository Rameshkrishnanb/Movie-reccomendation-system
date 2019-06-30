# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:12:51 2019

@author: Ramesh Krishnan B
"""
import pandas as pd
import numpy as np
from textblob.classifiers import NaiveBayesClassifier
from sklearn.model_selection import train_test_split
userid=414

#fr=open('ratings_20.csv')



ratings_data = pd.read_csv("F:/Project2/mllatestsmall/ratings_20.csv")  
ratings_data.head()

tags_data=pd.read_csv("F:/Project2/mllatestsmall/tags_modified.csv")
tags_data.head()

ratings_user=ratings_data[ratings_data['userId']==userid]
ratings_user=ratings_user[['movieId','rating']]
ratings_user=ratings_user.as_matrix()

rating_dict={}

for i in range(ratings_user.shape[0]):
    movieid=int(ratings_user[i,0])
    user_rating=ratings_user[i,1]
    if user_rating>3:
        rating_dict[movieid]=1
    else:
        rating_dict[movieid]=0

#-------------------------get traindata-------------------------------------------
traindata=[]
trainmovies=[]
#X=[]
#y=[]
fr=open('tags_modified.csv')
line=fr.readline()
count=0
testdata=[]
testresult=[]
for line in fr:
    movieid=int(line.split(',')[0])
    tags=line.split(',')[1].replace('\n','')
    if count==1500:
        break
    if movieid in rating_dict.keys():
        traindata.append((tags,rating_dict[movieid]))
        #trainmovies.append(movieid)
        testdata.append(tags)
        testresult.append(rating_dict[movieid])
        #X.append(tags)
        #y.append(rating_dict[movieid])
        count+=1
print(count,' number of movies available')
fr.close()

model=NaiveBayesClassifier(traindata)
#model.fit(traindata)
"""
#--------------------get testdata---------------------------------------
fr=open('tags_modified.csv')
line=fr.readline()
count=0
checkmovie=11
testdata=[]
testresult=[]
for line in fr:
    movieid=int(line.split(',')[0])
    tags=line.split(',')[1].replace('\n','')
    if int(movieid) in trainmovies:
    testdata.append(tags)
    testresult.append(rating_dict[movieid])    
print(count,' number of tests available')
fr.close()
"""

#-------------------------prediction--------------------------------------
z=[]
print('fitting done')
for data in testdata:
    z.append(model.classify(data))

diff=0

for a,b  in zip(testresult,z):
    if a!=b:
        diff+=1
        
print ('Difference is ',diff)
accuracy_score=((len(testdata)-diff)/len(testdata))
print('Accuracy score is ',accuracy_score)
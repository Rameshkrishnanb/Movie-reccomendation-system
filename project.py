# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 06:10:20 2019

@author: Ramesh Krishnan B
"""

import numpy as np  
import pandas as pd
userid =414
ratings_data = pd.read_csv("F:/Project2/mllatestsmall/ratings.csv")  
ratings_data.head()

movie_names = pd.read_csv("F:/Project2/mllatestsmall/movies.csv")  
movie_names.head() 

mergedata = pd.merge(ratings_data, movie_names, on='movieId')  
mergedata.head() 

#1----------------------------------
mergedata.groupby('title')['rating'].mean().head() 
mergedata.groupby('title')['rating'].count().sort_values(ascending=False).head()  
mergedata.groupby('title')['rating'].count().sort_values(ascending=False).head()
#2-----------------------------
ratings_mean_count = pd.DataFrame(mergedata.groupby('title')['rating'].mean()) 
ratings_mean_count['rating_counts'] = pd.DataFrame(mergedata.groupby('title')['rating'].count()) 

#try
'''z1=ratings_data[ratings_data['userId']==userid].sort_values('userId',ascending=True)
ratings_data.groupby['userid'].count()'''


#3graphs#-------------------------
import matplotlib.pyplot as plt  
import seaborn as sns  
sns.set_style('dark')  
#------'%matplotlib inline
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
#--------------#6
plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
ratings_mean_count['rating_counts'].hist(bins=50)  

plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
ratings_mean_count['rating'].hist(bins=50) 

plt.figure(figsize=(8,6))  
plt.rcParams['patch.force_edgecolor'] = True  
sns.jointplot(x='rating', y='rating_counts', data=ratings_mean_count, alpha=0.4)  

##7

user_movie_rating = mergedata.pivot_table(index='userId', columns='title', values='rating')
user_movie_rating.head()  
#8alladin
Alladin_ratings = user_movie_rating['Aladdin (1992)'] 
Alladin_ratings.head() 
#9movies like#------------------------
movies_like_Alladin = user_movie_rating.corrwith(Alladin_ratings)
corr_Alladin = pd.DataFrame(movies_like_Alladin, columns=['Correlation'])  
corr_Alladin.dropna(inplace=True)  
corr_Alladin.head()  

#tags elaborate----------------------------------------------------

#10
z=corr_Alladin.sort_values('Correlation', ascending=False) 

corr_Alladin = corr_Alladin.join(ratings_mean_count['rating_counts'])  
corr_Alladin.head() 

t1=corr_Alladin[corr_Alladin ['rating_counts']>20].sort_values('Correlation', ascending=False)
t1

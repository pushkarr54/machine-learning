# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:35:57 2023

@author: excel
"""

###############################################################################
import pandas as pd  
df = pd.read_csv('shopping_data.csv', delimiter=',') 
df.shape
df.head()
X = df.iloc[:, 3:5].values 
X.shape

# scatter plot
import matplotlib.pyplot as plt
plt.scatter(X[:,0],X[:,1])
plt.show()

## Forming a group using clusters
from sklearn.cluster import AgglomerativeClustering
cluster = AgglomerativeClustering(n_clusters=5, 
                                  affinity='euclidean', 
                                  linkage='ward')
Y = cluster.fit_predict(X)

Y = pd.DataFrame(Y)
Y.value_counts()

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))  
plt.scatter(X[:,0], X[:,1], c=cluster.labels_, cmap='rainbow')  


#===================================================================

from sklearn.cluster import KMeans
km = KMeans(n_clusters=6,n_init=20)

X = df.iloc[:, 2:5].values 

Y = km.fit_predict(X)
Y = pd.DataFrame(Y)
Y.value_counts()

km.inertia_
C = km.cluster_centers_

%matplotlib qt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='Red', s=1000) # S is star size, c= * color


clust = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(X)
    clust.append(kmeans.inertia_)

plt.scatter(range(1, 11), clust,color='red')
plt.plot(range(1, 11), clust)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('inertial values')
plt.show()

#===============================================
# DBSCAN
df

df.drop(['CustomerID','Genre'],axis=1,inplace=True)
array=df.values
array

from sklearn.preprocessing import StandardScaler
stscaler = StandardScaler().fit(array)
X = stscaler.transform(array)
X

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.75, min_samples=3)
dbscan.fit(X)

y = dbscan.labels_
y = pd.DataFrame(y)
y.value_counts()

cl=pd.DataFrame(dbscan.labels_,columns=['cluster'])
cl
clustered = pd.concat([df,cl],axis=1)
clustered

noisedata = clustered[clustered['cluster']==-1]
print(noisedata)
finaldata = clustered[clustered['cluster']==0]
finaldata

#=================================================

















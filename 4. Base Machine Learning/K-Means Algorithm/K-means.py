import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plot

data = pd.read_csv('Iris.csv')
data = data.iloc[:,1:-1].values
kmodel = KMeans(n_clusters=5, init='k-means++',random_state=0)
kmodel.fit(data)
tahmin = kmodel.predict(data)

merkezler = kmodel.cluster_centers_
print(merkezler)

plot.scatter(data[tahmin==0,0],data[tahmin==0,1],s=50,color='red')
plot.scatter(data[tahmin==1,0],data[tahmin==1,1],s=50,color='blue')
plot.scatter(data[tahmin==2,0],data[tahmin==2,1],s=50,color='green')
plot.scatter(data[tahmin==3,0],data[tahmin==3,1],s=50,color='purple')
plot.scatter(data[tahmin==4,0],data[tahmin==4,1],s=50,color='black')
plot.title('K-Means Iris Sınıflandırması')
plot.savefig('grafik.png')

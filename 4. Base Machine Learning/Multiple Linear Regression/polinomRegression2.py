import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('data.csv')


X = dataset.iloc[:, 1:3].values
y = dataset.iloc[:, 3].values

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X)


Lin_reg = LinearRegression()
Lin_reg.fit(X_poly,y)


fig, (ax0,ax1,ax2 ) = plt.subplots(nrows =3,figsize= (6,10))


ax0.scatter(X[:, 0:1], y, s=10, c='b', marker="o", label='first')
ax0.set_title("Seviye-maaş")
ax1.scatter(X[:, 1:2],y, s=10, c='r', marker="o", label='second')
ax1.set_title("Tecrübe-maaş")


#Polinom Lineer Regresyon Modeli
y_pred=Lin_reg.predict(X_poly)

y_len = len(y_pred)


for i in range(y_len):
    print(str(X[i]) +"| gerçek : "+ str(y[i]) +"| Tahmin ->" + str(y_pred[i]))

ax2.plot(y, label='gerçek',c='b')
ax2.plot(y_pred, label='tahmin', c='r')
plt.legend()

"""
ax2.plot(X[:, 0:1],y_pred,color="green",label="Polinom Regresyon Model")
ax3.plot(X[:, 1:2],y_pred,color="green",label="Polinom Regresyon Model")
ax2.legend()

"""

plt.show()
exit()


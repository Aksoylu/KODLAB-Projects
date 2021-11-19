''' Yüklü değil ise pip vasıtasıyla kurunuz:
pip install pandas
pip install numpy
pip install matplotlib
pip install sklearn
pip install sklearn.utils
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Sklearn içerisindeki lineer regresyon modeli
from sklearn.linear_model import LinearRegression

#Veri setimizi okuyoruz
dataset = pd.read_csv('veriseti.csv')

x = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values


#Lineer regresyon modelimizi eğitim için x-y ikilileri ile eğitiyoruz
lineer_regresyon_model = LinearRegression()
lineer_regresyon_model.fit(x,y)

#Test için ayırdığımız veri setine göre tahmin değerleri üretiyoruz

tahminEdilecekYillar = [[18],[19],[20],[21]] 
tahminSonuclari = lineer_regresyon_model.predict( tahminEdilecekYillar)

print(str(tahminEdilecekYillar) + " için sırasıyla tahmin sonuçları :" + str(tahminSonuclari) )

#Test verilerini grafik olarak görselleştirelim
plt.scatter(x, y, color ='blue')
plt.scatter(tahminEdilecekYillar, tahminSonuclari, color ='red')
plt.plot(x, lineer_regresyon_model.predict(x), color='green')
plt.title('Emisyon Salınımı Tahmini')
plt.xlabel('Yıl')
plt.ylabel('Emisyon Salınımı')
plt.show()
''' Yüklü değil ise pip vasıtasıyla kurunuz:
pip install pandas
pip install numpy
pip install sklearn
pip install sklearn.utils
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sklearn.utils
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv('veriseti.csv')
x = dataset.iloc[:, [1,2,3,4]].values
y = dataset.iloc[:, 1].values

for e in x:
    if e[0] == 'Erkek':
        e[0] = 1
    elif e[0] == 'Kadın':
        e[0] = 0




etiket = dataset.iloc[:, 5].values
scaler = StandardScaler()
scaler.fit(x)
parametre = scaler.transform(x)

from sklearn.tree import DecisionTreeClassifier 
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state=0)
classifier.fit(parametre, etiket)

print("Hastanın cinsiyetini girin : (kadın/erkek)")
cinsiyet = input()
if cinsiyet == "kadın":
    cinsiyet = 0
else:
    cinsiyet = 1
print("Hastanın yaşını girin :")
yas = int(input())
print("Hastanın Lökosit değerini (Akyuvar sayısını) girin :")
akyuvarSayisi = int(input())
print("Hastanın kronik bir rahatsızlığı var mı ? (evet/hayır)")
kronikRahatsizlik = input()
if kronikRahatsizlik=="evet":
    kronikRahatsizlik = 1
else:
    kronikRahatsizlik = 0
     
inputData = np.array([cinsiyet,yas, akyuvarSayisi, kronikRahatsizlik]).reshape(1, -1)


testVector = scaler.transform(inputData)
print(testVector)
print("-"*50)
predictionResult = classifier.predict(testVector)

if predictionResult == 1:
	print("Tahmin edilen durum: ağır seyir beklenilir")
if predictionResult == 0:
	print("Tahmin edilen durum: ayakta iyileşme beklenilir")

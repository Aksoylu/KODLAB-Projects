import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('covid19.csv')

dataset = dataset.drop(columns="ortalama_filyasyon_suresi")
dataset = dataset.drop(columns="yatak_doluluk_orani")
dataset = dataset.drop(columns="ortalama_temasli_tespit_suresi")
dataset = dataset.drop(columns="filyasyon_orani")
dataset = dataset.drop(columns="ventilator_doluluk_orani")
dataset = dataset.drop(columns="gunluk_test")
dataset = dataset.drop(columns="gunluk_iyilesen")
dataset = dataset.drop(columns="toplam_test")
dataset = dataset.drop(columns="toplam_hasta")
dataset = dataset.drop(columns="toplam_vefat")
dataset = dataset.drop(columns="toplam_iyilesen")
dataset = dataset.drop(columns="toplam_yogun_bakim")
dataset = dataset.drop(columns="toplam_entube")
dataset = dataset.drop(columns="hastalarda_zaturre_oran")  # Sabit olduğundan regresyonda bir önem ifade etmeyecektir.

#x :(bilinen veriler) gün, gunluk_vaka, gunluk_hasta, agir_hasta_sayisi, eriskin_yogun_bakim_doluluk_orani
#y :(gunluk_vefat)
dataset = dataset.dropna()
dataset = dataset[::-1].reset_index()
X = dataset.loc[:, [ "tarih" ,"gunluk_vaka", "gunluk_hasta", "agir_hasta_sayisi" , "eriskin_yogun_bakim_doluluk_orani"]]
y = dataset.loc[:, ["gunluk_vefat"]]

l = len(X.index)
for ind in X.index:
    X['tarih'][ind] = l-ind
    X["gunluk_vaka"][ind] = float(str(X["gunluk_vaka"][ind]).replace(".", ""))
    X["gunluk_hasta"][ind] = float(str(X["gunluk_hasta"][ind]).replace(".", ""))
    X["agir_hasta_sayisi"][ind] = float(str(X["agir_hasta_sayisi"][ind]).replace(".", ""))
    X["eriskin_yogun_bakim_doluluk_orani"][ind] = float(str(X["eriskin_yogun_bakim_doluluk_orani"][ind]).replace(",", ".") )
    #, yerine . olarak çevireceğiz ki float tipine dönüştürülebilsin

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

poly_reg = PolynomialFeatures(degree = 3)
X_poly = poly_reg.fit_transform(X)
Lin_reg = LinearRegression()
Lin_reg.fit(X_poly,y)


fig, (ax0,ax1,ax2 ) = plt.subplots(nrows =3,figsize= (6,10))

ax0.scatter(X.loc[:, ["tarih"]], y, s=10, c='b', marker="o", label='first')
ax0.set_title("Zaman-ölüm")

grafik__gunluk_vaka = X.loc[:, ["gunluk_vaka"]]
ax1.plot(grafik__gunluk_vaka, label='Günlük Vaka',c='r')
ax1.set_title("Günlük Vaka Sayısı")

grafik__gunluk_hasta = X.loc[:, ["gunluk_hasta"]]
ax2.plot(grafik__gunluk_hasta, label='Günlük Hasta',c='r')
ax2.set_title("Günlük Hasta Sayısı")


fig2, (bx0,bx1,bx2 ) = plt.subplots(nrows =3,figsize= (6,10))

grafik__agir_hasta = X.loc[:, ["agir_hasta_sayisi"]][::-1]
bx0.plot(grafik__agir_hasta, label='Ağır Hasta',c='r')
bx0.set_title("Ağır Hasta Sayısı")

grafik__eriskin_yogun_bakim_doluluk_orani = X.loc[:, ["eriskin_yogun_bakim_doluluk_orani"]]
bx1.plot(grafik__eriskin_yogun_bakim_doluluk_orani, label='Yoğun Bakım',c='r')
bx1.set_title("Yoğun Bakım Doluluk Oranı (%)")


#Polinom Lineer Regresyon Modeli
y_pred=Lin_reg.predict(X_poly)

bx2.plot(y, label='gerçek',c='b')
bx2.plot(y_pred, label='tahmin', c='r')
bx2.set_title("Gerçek - Tahmini Ölüm Sayıları")
plt.legend()

y_len = len(y_pred)
print(y_pred)
print(y_len, " adet gün için tahmin yapılmıştır")

for i in range(y_len):
    print("| gerçek : "+ str(y["gunluk_vefat"][i]) +"| Tahmin ->" + str(y_pred[i]))

def tarihDonustur(yeniTarih):
    from datetime import date
    dizi = yeniTarih.split(".")
    yeniTarih = date(int(dizi[2]), int(dizi[1]), int(dizi[0]))
    baslangicTarih = date(2021, 4, 16)
    fark = yeniTarih - baslangicTarih
    return fark.days

def tahminEt():
    print("---Covid 19 Polinom Regresyon Tahmin Mekanizması---")
    print("Tahmin edilecek tarihi girin (16.04.2021 ve sonrası)")
    tarih = input()
    fixTarih = tarihDonustur(tarih)
    print("Günlük Vaka sayısını girin")
    vakaSayi = int(input())
    print("Günlük semptomatik hasta sayısını girin")
    hastaSayi = int(input())
    print("Günlük ağır hasta sayısını girin")
    agirHastaSayi = int(input())
    print("Günlük yoğun bakım doluluk oranı girin")
    yogunBakimOran = int(input())
    tahmin_edilecek_veri = np.array([fixTarih,vakaSayi,hastaSayi,agirHastaSayi,yogunBakimOran] ).reshape(1,-1)
    tahmin_edilecek_veri = poly_reg.fit_transform(tahmin_edilecek_veri)
    tahmin = Lin_reg.predict(tahmin_edilecek_veri)
    print("'" +tarih +"' için Covid19 kaynaklı tahmini vefat sayısı :" + str(tahmin))


plt.show()


tarih = "18.07.2021"
fixTarih = tarihDonustur(tarih)
vakaSayi = 5000
hastaSayi = 2728
agirHastaSayi = 3558	
yogunBakimOran = 50

tahmin_edilecek_veri = np.array([fixTarih,vakaSayi,hastaSayi,agirHastaSayi,yogunBakimOran] ).reshape(1,-1)
tahmin_edilecek_veri = poly_reg.fit_transform(tahmin_edilecek_veri)

tahmin = Lin_reg.predict(tahmin_edilecek_veri)
print("'" +tarih +"' tarihi için Covid19 kaynaklı tahmini vefat sayısı :" + str(tahmin))


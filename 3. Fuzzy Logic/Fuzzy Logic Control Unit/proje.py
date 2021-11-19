#-- Fuzzy Logic Model Example--
# Author      : Umit Aksoylu
# Date        : 18.12.2020
# Description : Fuzzy Logic Modeling With Python & Numpy
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      :

import numpy as np
import fuzzyPy as fuzz
import matplotlib.pyplot as plt

#input degerleri tanimli oldugu araliklar
x_R = np.arange(0,91,1)
x_W = np.arange(0,11,1)
x_S = np.arange(0,151,1)
x_E = np.arange(0,21,1)

#output degerleri tanimli oldugu araliklar
x_O = np.arange(0,101,1)

#Yolun yapısı uyelik fonksiyonlari
R_kotu = fuzz.trapez(x_R, "SOL", [30, 45])
R_normal = fuzz.ucgen(x_R, [30, 45, 60])
R_iyi = fuzz.trapez(x_R, "SAG",[45, 60])


#Hava durumu uyelik fonksiyonlari
W_kotu = fuzz.ucgen(x_W, [0, 0, 5])
W_normal = fuzz.ucgen(x_W, [0, 5, 10])
W_iyi = fuzz.ucgen(x_W, [5, 10,10])

#Ortalama Hız uyelik fonksiyonlari
S_az = fuzz.ucgen(x_S, [0, 0, 70])
S_ort = fuzz.ucgen(x_S, [0, 70, 130])
S_cok = fuzz.trapez(x_S, "SAG",[70, 130])


#Kullanıcı Tecrübesi uyelik fonksiyonlari
E_az = fuzz.ucgen(x_E, [0, 0, 10])
E_ort = fuzz.ucgen(x_E, [0, 10, 20])
E_cok = fuzz.ucgen(x_E, [10, 20, 20])

#Çıkış, hız sınırı için uyelik fonksiyonlari
O_az = fuzz.trapez(x_O, "SOL", [25, 50])
O_ort = fuzz.ucgen(x_O,  [25, 50, 85])
O_cok = fuzz.trapez(x_O, "SAG",[50, 85])


# Input Grafiklerini Pylotlib ile render et.
fig, (ax0,ax1,ax2,ax3,ax4 ) = plt.subplots(nrows =5, figsize= (6,10))

# Yol viraj ve eğimi için grafik
ax0.plot(x_R,R_kotu, 'r', linewidth=2,label="Kötü")
ax0.plot(x_R,R_normal, 'g', linewidth=2,label="Normal")
ax0.plot(x_R,R_iyi, 'b', linewidth=2,label="İyi")
ax0.set_title("Yol viraj ve eğimi")
ax0.legend()

# Hava şartları için grafik
ax1.plot(x_W,W_kotu, 'r', linewidth=2,label="Kötü")
ax1.plot(x_W,W_normal, 'g', linewidth=2,label="Normal")
ax1.plot(x_W,W_iyi, 'b', linewidth=2,label="İyi")
ax1.set_title("Hava şartları")
ax1.legend()

# Sürücü ortalama hızı için grafik
ax2.plot(x_S,S_az, 'r', linewidth=2,label="Az")
ax2.plot(x_S,S_ort, 'g', linewidth=2,label="Orta")
ax2.plot(x_S,S_cok, 'b', linewidth=2,label="Çok")
ax2.set_title("Sürücü Ortalama Hızı")
ax2.legend()
# Kullanıcı tecrübesi için grafik
ax3.plot(x_E,E_az, 'r', linewidth=2,label="Kötü")
ax3.plot(x_E,E_ort, 'g', linewidth=2,label="Normal")
ax3.plot(x_E,E_cok, 'b', linewidth=2,label="İyi")
ax3.set_title("Kullanıcı Tecrübesi")
ax3.legend()

# Çıkış hız için grafik
ax4.plot(x_O,O_az, 'r', linewidth=2,label="Kötü")
ax4.plot(x_O,O_ort, 'g', linewidth=2,label="Normal")
ax4.plot(x_O,O_cok, 'b', linewidth=2,label="İyi")
ax4.set_title("Çıkış: Hız Sınırı")
ax4.legend()

plt.tight_layout()
plt.savefig('uyelik fonksiyonlari.png')
#Inputlari Al
print("Yol viraj düzeyi girin (0-90)")
input_R = input()
print("Hava durumu girin (0-10)")
input_W = input()
print("Sürücü ortalama hızı girin (30-150)")
input_S = input()
print("Kullanıcı deneyim yılı girin (0-20)")
input_E = input()

####### Input degerlerinin uyelik degerlerini hesapla #######
R_fit_kotu = fuzz.uyelik(x_R, R_kotu, input_R)
R_fit_normal = fuzz.uyelik(x_R, R_normal, input_R)
R_fit_iyi = fuzz.uyelik(x_R, R_iyi, input_R)

W_fit_kotu = fuzz.uyelik(x_W, W_kotu, input_W)
W_fit_normal = fuzz.uyelik(x_W, W_normal, input_W)
W_fit_iyi = fuzz.uyelik(x_W, W_iyi, input_W)

S_fit_az = fuzz.uyelik(x_S, S_az, input_S)
S_fit_ortalama = fuzz.uyelik(x_S, S_ort, input_S)
S_fit_cok = fuzz.uyelik(x_S, S_cok, input_S)

E_fit_az = fuzz.uyelik(x_E, E_az, input_E)
E_fit_ortalama = fuzz.uyelik(x_E, E_ort, input_E)
E_fit_cok = fuzz.uyelik(x_E, E_cok, input_E)


####### Kural Tanimlari #######


rule1 = np.fmin(np.fmin(R_fit_kotu, W_fit_kotu), O_az)
rule2 = np.fmin(np.fmin(R_fit_normal, W_fit_normal), O_ort)
rule3 = np.fmin(np.fmin(R_fit_iyi, W_fit_iyi), O_cok)
rule4 = np.fmin(np.fmax(S_fit_az , E_fit_az), O_az)
rule5 = np.fmin(np.fmax(S_fit_ortalama, E_fit_ortalama), O_ort)
rule6 = np.fmin(np.fmax(S_fit_cok, E_fit_cok), O_cok)

out_az = np.fmax(rule1,rule4)
out_ortalama = np.fmax(rule2,rule5)
out_cok = np.fmax(rule3,rule6)

####### Output Grafiklerini Pylotlib ile render et #######

O_zeros= np.zeros_like(x_O)
fig, grafik_output = plt.subplots(figsize= (7,4))
grafik_output.fill_between(x_O,O_zeros,out_az, facecolor ='r', alpha =0.7)
grafik_output.plot(x_O,O_az,'r', linestyle='--')
grafik_output.fill_between(x_O,O_zeros,out_ortalama, facecolor ='g', alpha =0.7)
grafik_output.plot(x_O,O_ort,'g', linestyle='--')
grafik_output.fill_between(x_O,O_zeros,out_cok,facecolor='b',alpha=0.7)
grafik_output.plot(x_O,O_cok, 'b', linestyle = '--')
grafik_output.set_title('Periyot Çıkışı :')
plt.tight_layout()
plt.savefig('cikis.png')


####### Output #######
print("-"*20)
mutlak_bulanik_sonuc = np.fmax(out_az,out_ortalama, out_cok)
durulastirilmis_sonuc = fuzz.durulastir(x_O,mutlak_bulanik_sonuc, 'agirlik_merkezi')

durulastirilmis_sonuc = durulastirilmis_sonuc * 3/2
print("duru sonuç->",durulastirilmis_sonuc)


sonuc_az = fuzz.uyelik(x_O,O_az, durulastirilmis_sonuc)
sonuc_orta = fuzz.uyelik(x_O,O_ort, durulastirilmis_sonuc)
sonuc_cok = fuzz.uyelik(x_O,O_cok, durulastirilmis_sonuc)
print("Duru Sonuç Üyelik Değerleri ---->Az:" ,sonuc_az, "| Orta:", sonuc_orta, "| Çok:" , sonuc_cok)

hizSiniri = 100


hizSiniri_dusuk = hizSiniri - ( sonuc_az* durulastirilmis_sonuc)
hizSinir_yuksek = hizSiniri + ( sonuc_cok * durulastirilmis_sonuc)

hizSiniri = (hizSiniri_dusuk + hizSinir_yuksek) /2

if(sonuc_az > sonuc_cok):
    hizSiniri = hizSiniri + ( sonuc_orta * durulastirilmis_sonuc) / 3
else:
    hizSiniri = hizSiniri - ( sonuc_orta * durulastirilmis_sonuc) / 3

degisim = hizSiniri - 100

print("Mevcut şartlar altında hız sınırı,", degisim, " değişerek " ,hizSiniri, " olmalıdır." )
print("Değişim oranı: %", float(degisim/100))
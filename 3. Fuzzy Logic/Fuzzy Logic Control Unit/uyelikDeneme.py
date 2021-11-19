#-- Fuzzy Logic Graphics Renderer--
# Author      : Umit Aksoylu
# Date        : 18.12.2020
# Description : Fuzzy Logic Model Rendering With Matplotlib
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      :

import numpy as np
import fuzzyPy as fuzz
import matplotlib.pyplot as plt



#input degerleri tanimli oldugu araliklar
x_B = np.arange(0,221,1)

#Boy uyelik fonksiyonlari
x_kisa = fuzz.ucgen(x_B, [-5000, 150, 165])
x_orta = fuzz.ucgen(x_B, [150, 165, 175])
x_uzun = fuzz.ucgen(x_B, [165, 175,5000])



# Input Grafiklerini Pylotlib ile render et.
fig, (ax0 ) = plt.subplots(nrows =1, figsize= (6,2))

# Yol viraj ve eğimi için grafik
ax0.plot(x_B,x_kisa, 'r', linewidth=2,label="Kısa")
ax0.plot(x_B,x_orta, 'g', linewidth=2,label="Orta")
ax0.plot(x_B,x_uzun, 'b', linewidth=2,label="Uzun")
ax0.set_title("Boy üyelik fonksiyonları")
ax0.legend()

plt.tight_layout()
plt.savefig('boy_uyelik.png')


print("Boy girin (cm)")
boy = input()

B_fit_kisa = fuzz.uyelik(x_B, x_kisa, boy)
B_fit_orta = fuzz.uyelik(x_B, x_orta, boy)
B_fit_uzun = fuzz.uyelik(x_B, x_uzun, boy)


print("Kısa üyelik : " + str(B_fit_kisa) )
print("Orta üyelik : " + str(B_fit_orta) )
print("Orta üyelik : " + str(B_fit_uzun) )
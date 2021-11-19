import cv2
import math
import warnings
import numpy as np


warnings.filterwarnings("ignore")

gorsel_1 = cv2.imread('görsel 1.png')
gorsel_2 = cv2.imread('görsel 2.png')

yukseklik = gorsel_1.shape[0]
genislik = gorsel_1.shape[1]

pixel_sayi = yukseklik * genislik

fark = 0

def pixelFark(pixel1,pixel2):
    pixel_fark = 0
    for i in range(3):
        pixel_fark = pixel_fark + abs(pixel1[i] - pixel2[i]) / 255
    return pixel_fark


for i in range(yukseklik):
    for j in range(genislik):
        fark = fark + pixelFark(gorsel_1[i][j],gorsel_2[i][j])

def farkMatris(matris1,matris2):
    yukseklik, genislik = matris1.shape[0], matris1.shape[1]
    matris = np.zeros(shape=(yukseklik, genislik, 3), dtype=np.uint8)

    for i in range(yukseklik):
        for j in range(genislik):
                if pixelFark(matris1[i][j],matris2[i][j]) <= 0:
                    matris[i,j,0] = 255
                    matris[i,j,1] = 255
                    matris[i,j,2] = 255
                    continue
                else:
                    matris[i,j,0] == matris2[i][j][0]
                    matris[i,j,1] == matris2[i][j][1]
                    matris[i,j,2] == matris2[i][j][2]
    img = Image.fromarray(matris, 'RGB')
    img.save('farkMatris.png')


farklilik_oran = 100 * fark / (genislik * yukseklik * 3)
print("İki görsel arasındaki farklılık oranı :" + str(farklilik_oran))
benzerlik_oran =   100 - farklilik_oran
print("İki görsel arasındaki benzerlik oranı :" + str(benzerlik_oran))
farkMatris(gorsel_1,gorsel_2)
print("İki görsel arasındaki farklılıklar, fark.png dosyası olarak kayıt edildi")





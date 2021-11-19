#     Mamdani Fuzzy Logic Libray From Scratch
# Author      : Umit Aksoylu
# Date        : 18.12.2020
# Description : Fuzzy Logic Mamdani Modeling
# Website     : http://umit.space
# Mail        : umit@aksoylu.space
# Github      :

import numpy as np

def trapez(x,rot,abc):

    y = np.zeros(len(x))

    if(rot == "ORTA"):
        assert len(abc) == 3, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
        a, b, c = np.r_[abc]
        assert a <= b and b <= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
        
        idx = np.nonzero(np.logical_and(x >= 0, x < a))[0]
        y[idx] = (x[idx] ) / float(a)

        idx = np.nonzero(np.logical_and(x >= a, x <b))[0]
        y[idx] = 1

        idx = np.nonzero(np.logical_and(x >= b, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

        print("!")
        return y

    else:
        assert len(abc) == 2, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
        a, b = np.r_[abc]     # Zero-indexing in Python
        if( rot == "SOL"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
            idx = np.nonzero(x < a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
            y[idx] = (x[idx] - b) / float(a - b)
            return y        
        elif (rot == "SAG"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
            idx = np.nonzero(x > a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x > a, x <= b))[0]
            y[idx] = (x[idx] - a) / float(b - a)
            return y        


def ucgen(x, abc):

    # a <= b <= c olmalıdır
    assert len(abc) == 3, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir !'
    a, b, c = np.r_[abc]     # Zero-indexing in Python
    assert a <= b and b <= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <=  Bitis'
    
    y = np.zeros(len(x))

    # Sol
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    # Sağ
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

    idx = np.nonzero(x == b)
    y[idx] = 1
    return y


#Gerçek bir değerin bir üyelik fonksiyonuna olan üyelik degerini hesaplayan fonksiyon
def uyelik(x, xmf, xx, zero_outside_x=True):
    if not zero_outside_x:
        kwargs = (None, None)
    else:
        kwargs = (0.0, 0.0)
    # Numpy'in İnterpolasyon Fonksiyonu:
    return np.interp(xx, x, xmf, left=kwargs[0], right=kwargs[1])



def durulastir(x, LFX, model):

    model = model.lower()
    x = x.ravel()
    LFX = LFX.ravel()
    n = len(x)
    if n != len(LFX):
        print("Bulanık Küme Üyeliği ve Değer Sayısı Eşit Olmalıdır.")
        return

    #     # 'agirlik_merkezi' : Ağırlık Merkezi Ortalama
    #     * 'maxort'          : maksimum ortalama
    #     * 'minom'           : en büyüklerin en küçüğü
    #     * 'maxom'           : en büyüklerin en büyüğü

    if 'agirlik_merkezi' in model:


        if 'agirlik_merkezi' in model:
            return agirlik_merkezi(x, LFX)

        elif 'AC0' in model:
            return 0    #AC0(x, mfx)   #todo, implement bisector AC0

    elif 'maxort' in model:
        return np.mean(x[LFX == LFX.max()])

    elif 'minom' in model:
        return np.min(x[LFX == LFX.max()])

    elif 'maxom' in model:
        return np.max(x[LFX == LFX.max()])




# 'Ağırlık Merkezi' Durulaştırma Metodu
def agirlik_merkezi(x, LFX):

    sum_moment_area = 0.0
    sum_area = 0.0

    # X dizisinin 1 elemanlı olduğu durum, tek bir bulanık kümeye üyeliğin olduğu durumdur.
    # Eğer Üyelik Fonksiyonu sadece tek bir bulanık kümeye üye ise de 
    # Ağırlık merkezi hesabı yapmaya gerek yoktur. kendi ağırlık alanı hesaplanıp döndürülür.
    if len(x) == 1:
        return x[0]*LFX[0] / np.fmax(LFX[0], np.finfo(float).eps).astype(float)

    # Birden fazla bulanık küme var ise;
    # İlgili üyelik değerinin çıkış kümesi üzerinde kestiği alanlar toplanır
    for i in range(1, len(x)):
        x1 = x[i - 1]
        x2 = x[i]
        y1 = LFX[i - 1]
        y2 = LFX[i]

        # Eğer y1 == y2 == 0.0 veya x1==x2 ise bu bir dikdörtgendir.
        if not(y1 == y2 == 0.0 or x1 == x2):
            if y1 == y2:  # Dikdörtgen alan ise :
                moment = 0.5 * (x1 + x2)
                area = (x2 - x1) * y1
            elif y1 == 0.0 and y2 != 0.0:  # Üçgen, yükseklik y2 ise :
                moment = 2.0 / 3.0 * (x2-x1) + x1
                area = 0.5 * (x2 - x1) * y2
            elif y2 == 0.0 and y1 != 0.0:  # Üçgen, yükseklik y1 ise :
                moment = 1.0 / 3.0 * (x2 - x1) + x1
                area = 0.5 * (x2 - x1) * y1
            else:                          # Diğer Koşullarda
                moment = (2.0 / 3.0 * (x2-x1) * (y2 + 0.5*y1)) / (y1+y2) + x1
                area = 0.5 * (x2 - x1) * (y1 + y2)

            # Toplam Alan += Hesaplanan Kesme Alanı
            sum_moment_area += moment * area
            sum_area += area

    return sum_moment_area / np.fmax(sum_area,
                                     np.finfo(float).eps).astype(float)
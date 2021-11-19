import random
def ortalamaHesapla(dizi):
    elemanSayi = len(dizi)
    if elemanSayi <= 1:
        return 0
    else:
        return sum(dizi) / elemanSayi

def standartSapmaHesapla(dizi):
    sapma = 0.0  
    elemanSayi = len(dizi)
    if elemanSayi <= 1:
        return 0
    else:
        for eleman in dizi:
            sapma += (float(eleman) - ortalamaHesapla(dizi)) ** 2
        sapma = (sapma / float(elemanSayi)) ** 0.5
        return sapma

def korelasyonBul(dizi1, dizi2):
    assert len(dizi1) == len(dizi2)
    elemanSayi = len(dizi1)
    assert elemanSayi > 0

    dizi_olasilik = 0
    dizi1_dagilim = 0
    dizi2_dagilim = 0
    for i in range(elemanSayi):
        dizi1_fark = dizi1[i] - ortalamaHesapla(dizi1)
        dizi2_fark = dizi2[i] - ortalamaHesapla(dizi2)
        dizi_olasilik += dizi1_fark * dizi2_fark
        dizi1_dagilim += dizi1_fark * dizi1_fark
        dizi2_dagilim += dizi2_fark * dizi2_fark
    # 4. Adım
    return dizi_olasilik / (dizi1_dagilim * dizi2_dagilim)**.5

dizi1 = sorted([random.randrange(1, 500, 1) for i in range(500)])
dizi2 = sorted([random.randrange(1, 500, 1) for i in range(500)])

print("korelasyon:")
print(korelasyonBul(dizi1,dizi2))
print("standart sapma -1:")
print(standartSapmaHesapla(dizi1))
print("standart sapma -2:")
print(standartSapmaHesapla(dizi2))
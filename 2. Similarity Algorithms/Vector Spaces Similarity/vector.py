

#0 ile 100 arasina sıkıştırıyoruz..
def arrange(item, dim,min,max):

    item_count,i = len(item),0

    for i in range(dim):
        if(i <= item_count):
            item[i] = item[i] / ((max - min) / 100) #percent value
        else:
            item[i] = 50 / ((max - min) /100 )
    return item


def kokal(x):
    return x**(1/2)


def usal(x,level):
    return x**level

#iki nokta arasi uzakligin hesaplanmasi
def vectorSimilarity(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ =len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] -  (A[i] ), 2 )
        distance = kokal(total)


        max_dist = 0
        for i in range(len_):
            max_dist += usal(100,2)
        max_dist = kokal(max_dist)


        return  1- (distance/ max_dist)   # dist/ max dist


    # uzakligi bul, en uzak uzakliga bol, %lik hale getir.
    return 0




kirmizi = [255,0,0]
koyuKirmizi = [181, 25, 25]
kahverengi = [48, 34, 15]
siyah = [0, 0, 0]
beyaz = [255, 255, 255]
gri = [82, 82, 82]

kirmizi_normalized = arrange(kirmizi, 3, 0, 255)
koyuKirmizi_normalized  = arrange(koyuKirmizi,3, 0, 255)
kahverengi_normalized = arrange(kahverengi,3, 0, 255)
siyah_normalized = arrange(siyah,3, 0, 255)
beyaz_normalized = arrange(beyaz,3, 0, 255)
gri_normalized= arrange(gri, 3, 0, 255)



#siyah_siyah_benzerlik_orani = vectorSimilarity(siyah_normalized,siyah_normalized)
#print("siyah-siyah benzerlik oranı:", siyah_siyah_benzerlik_orani)
#print(siyah_siyah_benzerlik_orani)


benzerlik_orani = vectorSimilarity(siyah_normalized,siyah_normalized)
print(benzerlik_orani)

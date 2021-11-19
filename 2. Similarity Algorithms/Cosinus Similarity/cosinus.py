#Etkisiz kelimeleri bul


def stopWord(kelime):
    stopWords = ["acaba", "ama", "ancak", "artık", "aslında", "az", "gene", "gibi", "da", "de", "en", "daha","diğer", "diğeri" , "diye", "dolayı"]  
    flag = True
    for i in range(len(stopWords)):
        if stopWords[i] == kelime:
            return True
        else:
            flag =False
    return flag

def ara(dizi,kelime):
    flag = False
    for eleman in dizi:
        if eleman == kelime:
            return True
        else:
            flag = False
    return flag


def sozlukOku(dizi):
    sozluk = []
    for cumle in dizi:
        kelimeler = cumle.split(" ")
        for kelime in kelimeler:
            if stopWord(kelime):
                continue
            else:
                if len(sozluk) == 0:
                    sozluk.append(kelime)
                else :
                    if ara(sozluk,kelime):
                        continue
                    else:
                        sozluk.append(kelime)
    return sozluk

def cumle2Vec(cumle,sozluk):
    vector = []

    kelimeler = cumle.split(" ")
    for sozcuk in sozluk:
        sozcukSayi = 0
        for kelime in kelimeler:
            if kelime == sozcuk:
                sozcukSayi = sozcukSayi + 1
        vector.append([sozcuk,sozcukSayi])

    return vector

    kelimeler = cumle.split(" ")
    for kelime in kelimeler:
        for t in range(len(sozluk)):
            if sozluk[t] == kelime:
                if len(vector) == 0:
                    vector.append([kelime, 1])
                else:
                    for i in range(len(vector)):
                        if vector[i][0] == kelime:
                            vector[i][1] = vector[i][1] + 1
                            break
                        else:
                            vector.append([kelime,1])
                            break
    return vector


cumle_1 = "merhabalar benim adım ümit"
cumle_2 = "selam benim adım zeynep"

print("1.Cümle :" + cumle_1)
print("2.Cümle :" + cumle_2)


sozluk = sozlukOku([cumle_1,cumle_2])

print(sozluk)
cumle_1_vector = cumle2Vec(cumle_1,sozluk)
cumle_2_vector = cumle2Vec(cumle_2,sozluk)

print(cumle_1_vector)
print(cumle_2_vector)

def noktasalCarpim(vector1,vector2):
    if len(vector1) != len(vector2):
        return -1

    toplam = 0
    for i in range(len(vector1)):
        toplam = toplam + vector1[i][1] * vector2[i][1]
    return toplam

def vectorBoyut(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam = toplam + (vector[i][1] * vector[i][1])

    return toplam ** (1/2)


def cosinusBenzerligi(vector1,vector2):
    return noktasalCarpim(vector1,vector2)  / ( vectorBoyut(vector1) * vectorBoyut(vector2) )


benzerlikOrani = cosinusBenzerligi(cumle_1_vector,cumle_2_vector)


print("İki cümle arası benzerlik oranı : " + str(benzerlikOrani))
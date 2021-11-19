def kokal(x):
    if x>0:
        return x**(1/2)
    else:
        return -1 * x**(1/2)

def usal(x,level):
    return x**level

def most_frequent(dizi): 
    counter = 0
    num = dizi[0] 
    for i in dizi: 
        curr_frequency = dizi.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
    return num 

def euclideanDistance(A,B):
    if len(A) != len(B):
        return -1
    else:
        len_ =len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] -  (A[i] ), 2 )
        distance = kokal(total)
        return distance

def KNNhesapla(uzay,ornek,n):
    
    tmp_ornekUzay = uzay.copy()
    tmp_ornekNokta = ornek.copy()
    tmp_ornekNokta.pop()
    komsular = []
    boyut = len(ornek) -1
    print("En yakın '" + str(n) + "' komşu :")
    for i in range(n):
        
        enYakinEleman = []
        for j in range(len(tmp_ornekUzay)):
            
            minimumMesafe = 1000

            for eleman in tmp_ornekUzay:

                tmp_eleman = eleman.copy()
                tmp_eleman.pop()    
                mesafe = euclideanDistance(tmp_eleman,tmp_ornekNokta)
                
                if mesafe <= minimumMesafe:
                    minimumMesafe = mesafe
                    enYakinEleman = eleman.copy()

        print(enYakinEleman)
        renk =  enYakinEleman[len(enYakinEleman)- 1]
        komsular.append(renk)
        tmp_ornekUzay.remove(enYakinEleman)

    print("Komşuların Renkleri :")
    print(komsular)
    
    return most_frequent(komsular)

A = [5,5,"mavi"]
B = [10, 10, "mavi"]
C = [25, 25, "kırmızı"]
D = [50, 50, "mavi"]
E = [100, 100, "kırmızı"]
F = [255, 255, "kırmızı"]

ornekUzay = [A,B,C,D,E,F]

print("Verinin X değerini girin")
x = int(input())
print("Verinin Y değerini girin")
y = int(input())

ornekNokta = [x,y,""]
ornekNoktaRenk = KNNhesapla(ornekUzay,ornekNokta,n = 3)
print("Seçilen noktanın rengi (Baskın Komşuluk Rengi): " + ornekNoktaRenk)

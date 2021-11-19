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

#iki nokta arası uzaklığı hesaplayan öklid benzerliğini hesaplayan fonksiyon
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



#Örnek uzay, örnek nokta ve N (komşuluk) sayısını parametre olarak alır.
def KNNhesapla(uzay,ornek,n):
    
    
    # Komşular listesine ekledikçe örnek uzaydan noktaları çıkaracağız.
    # Aynı şekilde, örnek noktanın son elemanı etiket verisi yani string bir değer olduğundan
    # öklid hesaplamasına katılmaması için çıkaracağız.

    # Bu nedenle örnek uzayı ve örnek noktamızı kopyalayarak çoğaltıyoruz.
    tmp_ornekUzay = uzay.copy()
    tmp_ornekNokta = ornek.copy()
    tmp_ornekNokta.pop()

    # En yakın 'N' adet komşunun etiket verisi (rengi) bu listede tutulacaktır.
    komsular = []
    boyut = len(ornek) -1
    print("En yakın '" + str(n) + "' komşu :")


    # En yakın 'N' adet komşu tespit edileceğinden, en yakın elemanı bulma işlemi N defa tekrarlanacak
    for i in range(n):
        
        
        enYakinEleman = []
        for j in range(len(tmp_ornekUzay)):
            
            # Başlangınçta minimum mesafe 1000 olarak tanımlıyoruz.
            minimumMesafe = 1000
            
            # Örnek noktamız ile uzaydaki tüm noktalar arasındaki mesafeyi kıyaslayan iç for döngüsü
            for eleman in tmp_ornekUzay:
                
                # Uzaydaki elemanların bir kopyası alınır ve etiket verisi (string) olan son indis çıkarılır
                tmp_eleman = eleman.copy()
                tmp_eleman.pop()    

                # Mevcut indisli örnek uzay noktası ile örnek nokta arasındaki mesafe hesaplanılır
                mesafe = euclideanDistance(tmp_eleman,tmp_ornekNokta)
                
                # Eğer mesafe en küçük mesafeye eşit veya küçük ise, minimmum mesafe güncellenir.
                # İç döngü dışındaki en yakın eleman değişkeni de mevcut indisli elemanın kopyası olarak atanır
                if mesafe <= minimumMesafe:
                    minimumMesafe = mesafe
                    enYakinEleman = eleman.copy()

        # Tespit edilen en yakın eleman yazdırılır.
        print(enYakinEleman)
        # En yakın elemanın rengi, komşular listesine eklenilir
        renk =  enYakinEleman[len(enYakinEleman)- 1]
        komsular.append(renk)

        # Kopya örnek uzaydan en yakın eleman silinir ve döngü başa döndürüşür.
        # Böylece bir sonraki en yakın elemanın da listeye alınabilir.
        #  Bu döngü toplamda N defa tetiklenir
        tmp_ornekUzay.remove(enYakinEleman)

    print("Komşuların Renkleri :")
    print(komsular)
    
    # komşular dizisi, N adet en yakın elemanın etiket (renk) verisini içermektedir.
    # önceden tanımladığımız ve dizide en çok tekrar eden elemanı döndürmeyi sağlayan most_frequent
    # fonksiyonu ile baskın renk tespit edilir. Bu, örnek noktamızın rengi olacaktır.
    return most_frequent(komsular)

# A noktası 12,30 koordinatlarında "kırmızı" renkli (etiketli) bir noktadır.
# A,B,C,D,E,F noktaları da renkleri ve koordinatları ile tanımlanmıştır.
# Bu örnek uzaydaki tüm veriler kırmızı veya mavi olarak etiketlenmiştir.
# Eğer isterseniz nokta sayısını arttırabilir, 2'den fazla etiket kullanabilirsiniz.
A = [5,5,"mavi"]
B = [10, 10, "mavi"]
C = [25, 25, "kırmızı"]
D = [50, 50, "mavi"]
E = [100, 100, "kırmızı"]
F = [255, 255, "kırmızı"]

# A,B,C,D,E,F noktaları örnek uzaya dahil edilir.
ornekUzay = [A,B,C,D,E,F]

while True:

    print("Yeni bir nokta için (y), tüm uzayı yazdırmak için (u) çıkmak için (x)")
    i = input()

    if i =="x":
        break
    elif i == "u":
        print(ornekUzay)
        continue
    elif i == "y":

        # Kullanıcıdan aldığımız koordinat verileri ile  örnek uzayda etiketi tespit edilmek üzere bir nokta seçeceğiz 
        print("Verinin X değerini girin")
        x = int(input())
        print("Verinin Y değerini girin")
        y = int(input())

        # ornek = [X,Y,ETİKET] verisinin ilk iki parametresi, iki boyutlu düzlemde koordinat ifade ederken
        # Son parametre olan "ETİKET", noktanın rengini ifade eder. Örnek verimizin rengini bilmiyoruz ve KNN algoritması ile
        # tespit etmek istiyoruz. Bu nedenle etiket parametresini boş bıraktık.
        ornekNokta = [x,y,""]


        # KNNcalculate fonksiyonu ile seçtiğimiz konumdaki örnek noktanın etiketini (rengini) tespit edeceğiz.
        ornekNoktaRenk = KNNhesapla(ornekUzay,ornekNokta,n = 3)

        # KNN algoritması, uzayın boyut sayısından bağımsızdır. Dolayısı ile ikiden çok parametreye sahip veriler arasında da 
        # KNN algoritmasını çalıştırabilirsiniz. Bu örneğimizde dikkat edilmesi gereken husus, son parametrenin etiket verisi olmasıdır.

        print("Seçilen noktanın rengi (Baskın Komşuluk Rengi): " + ornekNoktaRenk)

        #Rengi tespit edilen noktanın da örnek uzaya dahil edilmesini sağladık. Daha fazla veri ile daha spesifik sonuçlar elde edilebilir.
        ornekNokta[len(ornekNokta) -1] = ornekNoktaRenk
        
        #Eğer mevcut nokta zaten var ise ekleme

        mevcutluk = False
        for e in ornekUzay:

            tmp_e = e.copy()
            tmp_e.pop()
            tmp_o = ornekNokta.copy()
            tmp_o.pop()

            if tmp_e == tmp_o:
                mevcutluk = True
        
        if(mevcutluk == False):
            ornekUzay.append(ornekNokta)
        else:
            print(str(e) + " noktası zaten var etiketli uzaya eklenmedi")



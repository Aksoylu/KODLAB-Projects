import cv2

gorsel=cv2.imread("ornek3.png")

yukseklik, genislik = gorsel.shape[:2]   #Görüntüyü merkezin etrafında döndürmek için ikiye bölün.

dondurmeMatrisi = cv2.getRotationMatrix2D((yukseklik/2, genislik/2), -60,0.5)



gorsel = cv2.warpAffine(gorsel, dondurmeMatrisi, (yukseklik, genislik))


cv2.imwrite("dondurulmus.png",gorsel)
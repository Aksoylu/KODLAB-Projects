import cv2

gorsel =cv2.imread("ornek6.png")
Baslangic = (360,320)
Bitis = (510,370)
Renk = (255,0,0)
Kalinlik = 5
cv2.rectangle(gorsel,Baslangic,Bitis,Renk,Kalinlik)
cv2.imwrite("rectangleTest.png",gorsel)

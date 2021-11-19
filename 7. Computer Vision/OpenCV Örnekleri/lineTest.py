import numpy as np
import cv2

gorsel =cv2.imread("ornek4.png")
Baslangic = (100,300)
Bitis = (800,300)
Renk = (255,0,0)
Kalinlik = 5
cv2.line(gorsel,Baslangic,Bitis,Renk,Kalinlik)
cv2.imwrite("cizimTest.png",gorsel)

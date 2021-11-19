import numpy as np

gorsel=cv2.imread("ornek8.png")
yazilacakMetin = "ISTANBUL/ATAKOY"
koordinatlar = (300,400)
font = cv2.FONT_HERSHEY_SIMPLEX
fontBoyutu= 2
renk = (0,0,255)
kalinlik = 3
satirTipi = cv2.LINE_AA

cv2.putText(gorsel,yazilacakMetin,koordinatlar, font, fontBoyutu,renk,kalinlik,satirTipi)

cv2.imwrite("yaziTest.png",gorsel)
import cv2
import numpy as np
 
kamera = cv2.VideoCapture(0)
 
while(True):
    ret, kare = kamera.read()
 
    kare_hsv=cv2.cvtColor(kare,cv2.COLOR_BGR2HSV)
 
    mavi_baslangic=np.array([100,60,60])
    mavi_bitis=np.array([140,255,255])
 
 
    maskeleme=cv2.inRange(kare_hsv,mavi_baslangic,mavi_bitis)
    kare_filtrelenmis=cv2.bitwise_and(kare,kare,mask=maskeleme)
 
    cv2.imshow('Orjinal Kare',kare)
    cv2.imshow('Maskeli Kare',maskeleme)
    cv2.imshow('Filtrelenmis Kare',kare_filtrelenmis)
 
    if cv2.waitKey(25) & 0xFF == ord('x'):
        break
 
kamera.release()
cv2.destroyAllWindows() 
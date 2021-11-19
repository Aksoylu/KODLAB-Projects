import numpy as np
import cv2

gorsel=cv2.imread("ornek7.png")

koseNoktalari = np.array([[50,160],[125,160],[160,230],[10,230]], np.int32)
koseNoktalari = koseNoktalari.reshape((-1,1,2))
kapalilik = True
renk = (0,255,255)
kalinlik = 3
cv2.polylines(gorsel,[koseNoktalari],kapalilik,renk,kalinlik)
cv2.imwrite("poligonTest.png", gorsel)
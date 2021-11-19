import cv2
import numpy as np

gorsel =np.zeros((512,512,3), np.uint8)
Merkez = (220,220)
yariCap = 50
Renk = (255,0,0)
Kalinlik = -1
cv2.circle(gorsel,Merkez,yariCap,Renk,Kalinlik)
cv2.imwrite("circleTest.png",gorsel)

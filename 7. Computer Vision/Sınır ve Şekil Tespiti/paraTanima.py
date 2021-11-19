import numpy as np
import cv2

gorsel = cv2.imread('test3.png')


gorsel_gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)


_ , gorsel_gri = cv2.threshold(gorsel_gri, 240 , 255, cv2.CHAIN_APPROX_NONE)
konturlar , _ = cv2.findContours(gorsel_gri, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for kontur in konturlar:
    kenarSayi = cv2.approxPolyDP(kontur, 0.01* cv2.arcLength(kontur, True), True)
    
    x = kenarSayi.ravel()[0]
    y = kenarSayi.ravel()[1] - 5

    x, y , w, h = cv2.boundingRect(kenarSayi)
    
    if h <100:
        continue
    
    else:
        if len(kenarSayi) >= 12 :
            
            if w > 180:
                cv2.putText(gorsel, "1 Lira", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            elif w< 180 and w>150:
                cv2.putText(gorsel, "50 KR", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            elif w< 160 and w>130:
                cv2.putText(gorsel, "25 KR", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            elif h< 140 and h>110:
                cv2.putText(gorsel, "10 KR", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            elif w< 130:
                cv2.putText(gorsel, "1 KR", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            else:
                cv2.putText(gorsel, "para", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    print(w)
    gorsel = cv2.drawContours(gorsel, [kenarSayi], 0, (255, 0, 0), 5)
cv2.imshow('Sekiller', gorsel)


cv2.waitKey(0)
cv2.destroyAllWindows()
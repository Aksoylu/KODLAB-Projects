import numpy as np
import cv2

gorsel = cv2.imread('test.png')
gorsel_gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)


_ , gorsel_gri = cv2.threshold(gorsel_gri, 240 , 255, cv2.CHAIN_APPROX_NONE)
konturlar , _ = cv2.findContours(gorsel_gri, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


for kontur in konturlar:
    kenarSayi = cv2.approxPolyDP(kontur, 0.01* cv2.arcLength(kontur, True), True)
    gorsel = cv2.drawContours(gorsel, [kenarSayi], 0, (0, 0, 0), 5)
    x = kenarSayi.ravel()[0]
    y = kenarSayi.ravel()[1] - 5

    if len(kenarSayi) == 3:
        cv2.putText( gorsel, "Ucgen", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX,1, (0, 0, 0) )
    elif len(kenarSayi) == 4 :
        x, y , w, h = cv2.boundingRect(kenarSayi)
        aspectRatio = float(w)/h
        print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio < 1.05:
            cv2.putText(gorsel, "Kare", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
            
        else:
            cv2.putText(gorsel, "Dortgen", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX,1, (0, 0, 0))
            
    elif len(kenarSayi) == 5 :
        cv2.putText(gorsel, "Besgen", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        
    elif len(kenarSayi) == 10 :
        cv2.putText(gorsel, "Yildiz", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
     
    else:
        cv2.putText(gorsel, "cember", (x+50, y+50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

cv2.imshow('Sekiller', gorsel)
cv2.waitKey(0)
cv2.destroyAllWindows()
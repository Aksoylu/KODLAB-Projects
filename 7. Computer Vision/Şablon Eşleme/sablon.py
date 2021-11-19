import cv2
import numpy as np

gorsel = cv2.imread('gorsel.png')
gorsel_gri = cv2.cvtColor(gorsel, cv2.COLOR_BGR2GRAY)

sablon = cv2.imread('sablon.png',0)
w, h = sablon.shape[::-1]

eslestirme = cv2.matchTemplate(gorsel_gri,sablon,cv2.TM_CCOEFF_NORMED)
esik = 0.7
uygunSonuc = np.where( eslestirme >= esik)
for nokta in zip(*uygunSonuc[::-1]):
    cv2.rectangle(gorsel, nokta, (nokta[0] + w, nokta[1] + h), (0,255,255), 2)

gorsel = cv2.resize(gorsel,(1200,760))
cv2.imshow('Eslestirme',gorsel)

cv2.waitKey(0)
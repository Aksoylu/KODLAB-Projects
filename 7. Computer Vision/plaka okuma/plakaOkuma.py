import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

kare = cv2.imread('test4.png',cv2.IMREAD_COLOR)
kare = cv2.resize(kare, (600,400) )

kare_gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY) 
kare_gri = cv2.bilateralFilter(kare_gri, 13, 15, 15) 

kenarlar = cv2.Canny(kare_gri, 30, 200) 
konturlar = cv2.findContours(kenarlar.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
konturlar = imutils.grab_contours(konturlar)
konturlar = sorted(konturlar, key = cv2.contourArea, reverse = True)[:10]
plakaKonveks = None

for kontur in konturlar:
    
    deger = cv2.arcLength(kontur, True)
    bulunan = cv2.approxPolyDP(kontur, 0.018 * deger, True)
 
    if len(bulunan) == 4:
        plakaKonveks = bulunan
        break

if plakaKonveks is None:
    tespitDegeri = 0
    print ("No contour detected")
else:
     tespitDegeri = 1

if tespitDegeri == 1:
    cv2.drawContours(kare, [plakaKonveks], -1, (0, 0, 255), 3)

maske = np.zeros(kare_gri.shape,np.uint8)
kare_yeni = cv2.drawContours(maske,[plakaKonveks],0,255,-1,)
kare_yeni = cv2.bitwise_and(kare,kare,mask=maske)

(x, y) = np.where(maske == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
plakaMatris = kare_gri[topx:bottomx+1, topy:bottomy+1]

okunulanMetin = pytesseract.image_to_string(plakaMatris, config='--psm 11')
print("Plaka:",okunulanMetin)
kare = cv2.resize(kare,(500,300))
plakaMatris = cv2.resize(plakaMatris,(400,200))
cv2.imshow('arac', kare)
cv2.imshow('kirpilmis', plakaMatris)


cv2.waitKey(0)
#testConfig
cv2.destroyAllWindows()
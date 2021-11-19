import cv2
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


plaka_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_russian_plate_number.xml')

kare = cv2.imread("test3.png")
kare = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

plakalar = plaka_cascade.detectMultiScale(kare, 1.3, 5)



for(x,y,w,h) in plakalar:
    kare = cv2.rectangle(kare,(x,y), (x + w , y+ h), (255,255,255),4)
    plaka =  kare[y + 4  :h + y  - 4 , x + 4 :w + x - 4]
    print(pytesseract.image_to_string(plaka))


cv2.imshow("plaka-okuyucu2", kare)
while True:
    k = cv2.waitKey(30) & 0xff
    if  k ==27:
        cv2.destroyAllWindows()
        break



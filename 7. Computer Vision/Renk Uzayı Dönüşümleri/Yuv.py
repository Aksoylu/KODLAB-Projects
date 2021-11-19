import cv2
  
gorsel = cv2.imread('test.png')
cikti_gorsel = cv2.cvtColor(gorsel, cv2.COLOR_BGR2YUV)
  
cv2.imshow('Orijinal Gorsel',gorsel)
cv2.imshow('Islem Sonrasi Gorsel', cikti_gorsel)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# Yazılara arka plan olması için siyah bir zemin oluşturalım.
# Siyah zemin, üç kanallı sıfırlarla dolu bir numpy matrisidir.
zemin = np.zeros((500,1000,3), np.uint8)  

metin = "Merhaba OpenCV kutuphanesi "  

cv2.putText(zemin,  
        "Hershey Simplex : " + metin,  
        (20, 40),  
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Plain : " + metin,  
        (20, 80),  
        fontFace=cv2.FONT_HERSHEY_PLAIN,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Duplex : " + metin,  
        (20, 120),  
        fontFace=cv2.FONT_HERSHEY_DUPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Complex : " + metin,  
        (20, 160),  
        fontFace=cv2.FONT_HERSHEY_COMPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Triplex : " + metin,  
        (20, 200),  
        fontFace=cv2.FONT_HERSHEY_TRIPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Complex Small : " + metin,  
        (20, 240),  
        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Script Simplex : " + metin,  
        (20, 280),  
        fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.putText(zemin,  
        "Hershey Script Complex : " + metin,  
        (20, 320),  
        fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,  
        fontScale=1,  
        color=(255, 255, 255))  

cv2.imshow('Fonts', zemin)  
cv2.waitKey(0)  

cv2.destroyAllWindows()  
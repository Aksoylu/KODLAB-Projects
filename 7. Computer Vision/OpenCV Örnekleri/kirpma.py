import cv2

gorsel=cv2.imread("ornek1.png")

kirpilmis=gorsel[0:200 , 0:100]

cv2.imwrite("kirpilmis.png",kirpilmis)
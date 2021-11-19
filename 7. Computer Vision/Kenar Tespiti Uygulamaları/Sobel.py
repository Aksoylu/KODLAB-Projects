import cv2

gorsel = cv2.imread("test.png")
sobel_yatay = cv2.Sobel(gorsel, cv2.CV_64F, 1, 0, ksize=5)
sobel_dikey = cv2.Sobel(gorsel, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("Normal Gorsel",gorsel)
cv2.imshow("Yatay Sobel Uygulanmis Gorsel",sobel_yatay)
cv2.imshow("Dikey Sobel Uygulanmis Gorsel",sobel_dikey)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

gorsel = cv2.imread("test.png")
laplacian = cv2.Laplacian(gorsel, cv2.CV_64F)

cv2.imshow("Normal Gorsel",gorsel)
cv2.imshow("Laplacian Uygulanmis Gorsel",laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
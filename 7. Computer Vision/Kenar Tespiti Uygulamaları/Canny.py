import cv2

gorsel = cv2.imread("test.png")
canny = cv2.Canny(gorsel, 200, 500)

cv2.imshow("Normal Gorsel",gorsel)
cv2.imshow("Laplacian Uygulanmis Gorsel",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()


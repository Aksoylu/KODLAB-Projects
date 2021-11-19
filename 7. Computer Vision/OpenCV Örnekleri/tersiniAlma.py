import cv2
gorsel=cv2.imread("ornek4.png")
en,boy = gorsel.shape[:2]

for x in range(en):
    for y in range(boy):
        for i in range(3):
            gorsel[x][y][i] = 255 - gorsel[x][y][i]

cv2.imwrite("ters.png",gorsel)
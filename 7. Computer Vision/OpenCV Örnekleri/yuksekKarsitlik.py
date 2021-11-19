import cv2
gorsel=cv2.imread("ornek5.png")
en,boy = gorsel.shape[:2]

basamakSayi = 4

basamakDeger = int(255/basamakSayi)

for x in range(en):
    for y in range(boy):
        max = 0
        max_indis = 0
        for i in range(3):
            pikselDeger = gorsel[x][y][i]
            if(pikselDeger > max):
                max = pikselDeger
                max_indis = i
        bolum = int(max / basamakDeger)
        gorsel[x][y] = [0,0,0]
        gorsel[x][y][max_indis] = basamakDeger *bolum


cv2.imwrite("karsit.png",gorsel)
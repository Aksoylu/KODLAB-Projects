import cv2

def serbestDonusum(genislik,yukseklik):
    gorsel=cv2.imread("ornek2.png")
    boyutlar = (genislik,yukseklik)
    gorsel = cv2.resize(gorsel,boyutlar,interpolation = cv2.INTER_CUBIC)
    cv2.imwrite("yenidenBoyutlandirilmis.png",gorsel)

def yuzdelikDonusum():

    gorsel=cv2.imread("ornek2.png")
    en,boy = gorsel.shape[:2]
    print("Mevcut en:",en, "\nYeni en değeri girin")
    yeniEn = int(input())
    degisimOrani =  yeniEn / en
    en = int(en * degisimOrani)
    boy = int(boy * degisimOrani)
    boyutlar = (en,boy)
    gorsel = cv2.resize(gorsel,boyutlar,interpolation = cv2.INTER_CUBIC)
    cv2.imwrite("yenidenBoyutlandirilmis.png",gorsel)
    print("Yeni boyutlar :", boyutlar)
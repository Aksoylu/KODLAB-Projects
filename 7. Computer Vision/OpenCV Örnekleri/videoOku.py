import cv2 as cv


video = cv.VideoCapture('testVideo.mp4')
 

# Dosyadan Görüntü okuma başarılı olduğu sürece while döngüsü çalışsın.
while(video.isOpened()):
    #Bir kare oku
    ret, frame = video.read()
    # Gri formatta okumak için
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame',frame)
    # q tuşuna basıldığında çık.
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
#Videoyu bırak ve pencereleri kapat
video.release()
cv.destroyAllWindows()
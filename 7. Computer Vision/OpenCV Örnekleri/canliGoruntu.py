import cv2

video = cv2.VideoCapture(0)

# codec tanımlama ve VideoWriter nesnesi oluşturma bilgi için bkz: https://www.fourcc.org/codecs.php
fourcc = cv2.VideoWriter_fourcc(*'XVID')
 

# Kaydedilecek video dosyasının adı, uzantısı, konumu, saniyedeki çerçeve sayısı ve çözünürlüğü
kaydedici = cv2.VideoWriter('kaydedilmisVideo.avi',fourcc, 30.0, (640,480))

while(video.isOpened()):
    basarili , kare = video.read()
 
    # Görüntü okuma başarılı ise
    if basarili ==True:
        # Döndürülen görüntüyü video dosyasına yaz.
        cv2.putText(kare,"KODLAB",(320,460),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255,255),2,cv2.LINE_4)
        kaydedici.write(kare)
        cv2.imshow('Video',kare)
 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
 
cap.release()
kaydedici.release()
cv.destroyAllWindows()
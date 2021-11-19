import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('mouth.xml')
nose_cascade = cv2.CascadeClassifier('nose.xml')
capt = cv2.VideoCapture(0)



while True:
    basarili, kare = capt.read()

    if basarili==False:
        break
    kare_gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(kare_gri, 1.3, 5)

    for(x,y,w,h) in faces:
        cv2.rectangle(kare,(x,y), (x + w , y+ h), (0,255,0),4)
        yuz_renkli = kare[y:y+h, x: x+w]
        yuz_gri = kare_gri[y:y+h, x: x+w]
        eyes =eye_cascade.detectMultiScale(yuz_gri)
        
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(yuz_renkli,(ex,ey), (ex + ew , ey+ eh), (0,0,255),4)
        nose = nose_cascade.detectMultiScale(yuz_gri)
        for(nx,ny,nw,nh) in nose:
            cv2.rectangle(yuz_renkli,(nx,ny), (nx + nw , ny+ nh), (255,255,255),4)
            break
        mouth = mouth_cascade.detectMultiScale(yuz_gri)
        for(mx,my,mw,mh) in mouth:
            cv2.rectangle(yuz_renkli,(mx,my), (mx + mw , my+ mh), (255,0,0),4)
            break


    cv2.imshow("haar-cascade siniflandiricisi", kare)
    k = cv2.waitKey(30) & 0xff

    if  k ==27:
        break
capt.release()
cv2.destroyAllWindows()

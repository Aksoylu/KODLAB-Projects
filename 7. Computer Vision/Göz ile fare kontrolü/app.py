import cv2
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#pip3 install pyautogui
import pyautogui as fare
fare.FAILSAFE = False



face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

capt = cv2.VideoCapture(0)

blink_model = tf.keras.models.load_model('blink-model.h5')


while True:
    basarili, kare = capt.read()

    if basarili==False:
        break

    kare_gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(kare_gri, 1.3, 5)
    if(len(faces) == 0):
        cv2.imshow("fare-kontrol", kare)
        k = cv2.waitKey(30) & 0xff
        if  k ==27:
            break

        continue

    yuz_sayisi = 0
    for(x,y,w,h) in faces:
        yuz_sayisi += 1

        if(yuz_sayisi ==2):
            yuz_sayisi = 0
            continue

        cv2.rectangle(kare,(x,y), (x + w , y+ h), (0,255,0),4)
        yuz_gri = kare_gri[y:y+h, x: x+w]
        yuz_renkli = kare[y:y+h, x: x+w]
        eyes =eye_cascade.detectMultiScale(yuz_gri)
    
        goz_sayi = 0
        son_ex, son_ey,son_ew,son_eh = -1,-1,-1,-1
        gozArray = []
        

        for(ex,ey,ew,eh) in eyes:
            goz_sayi+=1
            eye = [ex,ey,ew,eh]
            gozArray.append(eye)

        if( goz_sayi ==2):

            if(gozArray[0][0] > gozArray[1][0]):
                solGoz = gozArray[0]
                sagGoz = gozArray[1]
            else:
                solGoz = gozArray[1]
                sagGoz = gozArray[0]   

            solGoz_ex,solGoz_ey,solGoz_ew,solGoz_eh = solGoz
            sagGoz_ex,sagGoz_ey,sagGoz_ew,sagGoz_eh = sagGoz

            cv2.rectangle(yuz_renkli, (solGoz_ex,solGoz_ey), (solGoz_ex+solGoz_ew,solGoz_ey+solGoz_eh), (0,0,255),2)
            cv2.rectangle(yuz_renkli, (sagGoz_ex,sagGoz_ey), (sagGoz_ex+sagGoz_ew,sagGoz_ey+sagGoz_eh), (0,0,255),2)

            solGoz_matris = yuz_renkli[solGoz_ey + 4  :solGoz_eh + solGoz_ey  - 4 , solGoz_ex + 4 :solGoz_ew + solGoz_ex - 4]
            sagGoz_matris = yuz_renkli[sagGoz_ey + 4  :sagGoz_eh + sagGoz_ey  - 4 , sagGoz_ex + 4 :sagGoz_ew + sagGoz_ex - 4]
            
            x_offset=y_offset=20
            #solGoz_matris = cv2.cvtColor(solGoz_matris,cv2.COLOR_BGR2GRAY)
            kare[y_offset:y_offset+solGoz_matris.shape[0], x_offset:x_offset+solGoz_matris.shape[1]] = cv2.cvtColor(solGoz_matris, cv2.COLOR_BGR2RGB)
            
            x_offset=60
            kare[y_offset:y_offset+sagGoz_matris.shape[0], x_offset:x_offset+sagGoz_matris.shape[1]] = cv2.cvtColor(sagGoz_matris, cv2.COLOR_BGR2RGB)
            
            girisBoyut = 224
            
            solGoz_matris = cv2.resize(solGoz_matris, (girisBoyut, girisBoyut))
            solGoz_modelGiris = np.array(solGoz_matris).reshape(1, girisBoyut, girisBoyut, 3)
            solGoz_modelGiris = solGoz_modelGiris/255.0
            solGoz_icin_tahmin = blink_model.predict(solGoz_modelGiris)


            #sagGoz_matris = cv2.cvtColor(sagGoz_matris, cv2.COLOR_GRAY2BGR)
            sagGoz_matris = cv2.resize(sagGoz_matris, (girisBoyut, girisBoyut))
            sagGoz_modelGiris = np.array(sagGoz_matris).reshape(1, girisBoyut, girisBoyut, 3)
            sagGoz_modelGiris = sagGoz_modelGiris/255.0
            sagGoz_icin_tahmin = blink_model.predict(sagGoz_modelGiris)


            solGoz_icin_tahmin = float(solGoz_icin_tahmin[0][0])
            sagGoz_icin_tahmin = float(sagGoz_icin_tahmin[0][0])


            
            if(solGoz_icin_tahmin >= 0.95):
                print("Sol gözde kırpma algılandı")
                fare.click(button='left')

            if(sagGoz_icin_tahmin>= 0.95):
                print("Sağ gözde kırpma algılandı")
                fare.click(button='right')

            ort_ex = (solGoz_ex - sagGoz_ex) /2 + sagGoz_ex
            ort_ey = (solGoz_ey - sagGoz_ey) /2 + sagGoz_ey
            
            oran_ex = x/kare.shape[0]
            oran_ey = y/kare.shape[1]

            ekranBoyut = fare.size()

            fare_konum_x = int(ekranBoyut[0] * oran_ex)
            fare_konum_y = int(ekranBoyut[1] * oran_ey)

            if(fare_konum_x > 0 and fare_konum_x < ekranBoyut[0] and fare_konum_y >0 and fare_konum_y < ekranBoyut[1]):
                fare.moveTo(fare_konum_x,fare_konum_y)




        cv2.imshow("fare-kontrol", kare)
        k = cv2.waitKey(30) & 0xff

        if  k ==27:
            break

capt.release()
cv2.destroyAllWindows()






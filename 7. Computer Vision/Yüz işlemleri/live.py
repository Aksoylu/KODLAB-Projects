import cv2
import numpy as np
from PIL import Image as im
#pip3 install pywebview
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

capt = cv2.VideoCapture(0)
landmark_detector = cv2.face.createFacemarkLBF()
landmark_detector.loadModel("landmark.yaml")


def drawLandmark(img,landmarks,color):
    color_main  = color
    for landmark in landmarks:
        array = landmark[0]
        i = 0
        for l in array:
            x = l[0]
            y = l[1]

            #0-16  = cene hatti
            #16-21 = sol kas hatti
            #21-26 = sag kas hatti
            #26-30 = burun kemik hatti
            #30-35 = alt burun hatti
            #35-41 = sol goz hatti
            #41-47 = sag goz hatti
            #47-60 = agiz atti
            #59-68 = dudak hatti

            #cene
            if i <= 15 and i>=0:

                if i==0:
                    face_left = [x,y]

                if i==8:
                    chin_down= [x,y]
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]),color_main, 3)

            #sol kas
            if i<=20 and i >16:

                if i== 17:
                    left_eyebrow_left = [x,y]
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 4)

            if i==21:
                left_eyebrow_right = [x,y]

            #sag kas
            if i<=25 and i >21:
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 4)
                if i ==22:
                    right_eyebrow_left = [x,y]

            if i ==26:
                 right_eyebrow_right=  [x,y]

            #burun kemigi
            if i<=29 and i >26:
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]),color_main, 6)

            #alt burun
            if i<=34 and i >30:

                if i==31:
                     nose_left = [x,y]

                if i==33:
                     nose_bottom = [x,y]

                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 4)

            if i==35:
                nose_right = [x,y]

            #sol goz konveks
            if i<=40 and i >35:
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 2)


                if i== 36:  #start left eye
                    left_eye_left = [x,y]

                if i== 39:  #end left eye
                    left_eye_right = [x,y]

                if i == 40:
                    cv2.line(img, (array[36][0],array[36][1]),(array[41][0], array[41][1]), color_main, 2)

            #sag goz konveks
            if i<=46 and i >41:
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 2)


                if i== 42:  #start left eye
                    right_eye_left = [x,y]

                if i== 45:  #end left eye
                    right_eye_right = [x,y]

                if i == 46:
                    cv2.line(img, (x,y),(array[42][0], array[46][1]),color_main, 2)

            if i==48:
                mouth_left = [x,y]

            #agiz
            if i<=59 and i >48:
                if i==54:
                    mouth_right = [x,y]

                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 4)
                if i == 59:
                    cv2.line(img, (array[48][0],array[48][1]),(array[50][0], array[50][1]), color_main, 4)
            #dudak
            if i<=62 and i >60:
                cv2.line(img, (x,y),(array[i+1][0], array[i+1][1]), color_main, 4)

            if i==16:
                face_right = [x,y]

            i = i + 1


            if i == 68:
                break

    return img

def drawLandmarks(img,landmarks,color):

    for landmarkArray in landmarks[0]:
        for landmark in landmarkArray:
            coord = (int(landmark[0]), int(landmark[1]))
            cv2.circle(img,coord,1,color,5)
    return img

while True:
    basarili, kare = capt.read()

    if basarili==False:
        break
    kare_gri = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(kare_gri, 1.3, 5)
    kare_masked = kare.copy()
    for(x,y,w,h) in faces:
        cv2.rectangle(kare,(x,y), (x + w , y+ h), (0,255,0),4)
        yuz_renkli = kare[y:y+h, x: x+w]
        yuz_gri = kare_gri[y:y+h, x: x+w]
        _, landmarks = landmark_detector.fit(kare_gri, faces)
        w,h = kare_gri.shape
        blank = np.zeros((w,h,3), np.uint8)

        print(blank)
        kare_masked = drawLandmark(blank,landmarks,(255,255,255))
        kare = drawLandmark(kare,landmarks,(255,255,255))
        break

    cv2.imshow("Serbest",kare)
    cv2.imshow("Maskeli",kare_masked)

    #cv2.imshow("fare-kontrol", kare)
    k = cv2.waitKey(30) & 0xff

    if  k ==27:
        break
capt.release()
cv2.destroyAllWindows()

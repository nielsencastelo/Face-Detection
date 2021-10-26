# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:03:04 2021

@author: Nielsen Castelo Damasceno
"""

import cv2
import time
#import imutils

#DIMENSAO = 720
totalFrames = 0
skip_frames = 1
url = 'rtsp://admin:globalsys123@192.168.0.64:554/Streaming/channels/101/'

cap = cv2.VideoCapture(url)


#fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#out = cv2.VideoWriter('output_real_time.avi',fourcc, 20.0, (1280,720))
#out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10,(1280,720))
#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
size = (width, height)
fps = cap.get(cv2.CAP_PROP_FPS)



fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('your_video.avi', fourcc, fps, size)

detector_facial = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

time.sleep(1.0)
while True:
    ret, frame = cap.read()
    
    if not (ret):
        print('Erro no frame')
        st = time.time()
        cap = cv2.VideoCapture(url)
        #cap = cv2.VideoCapture(0)
        print("tempo perdido devido à inicialização  : ",time.time()-st)
        continue
    
    if ret == True:
        if totalFrames % skip_frames == 0:
            
            #frame = imutils.resize(frame, width=DIMENSAO)
            
            # detectar as faces
            imagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            deteccoes = detector_facial.detectMultiScale(imagem_cinza, scaleFactor=1.09)
            
            for x, y, w, h in deteccoes:
                #print(x, y, w, h)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,255), 5)
            
            out.write(frame)
            cv2.imshow('Imagem Real time', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
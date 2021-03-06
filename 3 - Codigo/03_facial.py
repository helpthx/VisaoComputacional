''''
Real Time Face Recogition
Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    
Developed by João Vitor Rodrigues Baptista  
'''

import cv2
import numpy as np
import os 
import time
from datetime import datetime
import sqlite3
import sys
from fuctions import Real_time_fuctions

c = Real_time_fuctions()

#Working with the local database
c.convert_list()

#Confidence
const = 100
confidence_in = const - 70 #Up to 70% will have acess
confidence_out = const - confidence_in

# Amout of money to access the rest
amout_money = 5.20


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#Inicial account
id = 0

#Init real time video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

#Define smallest square for wich face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)


#Main application loop
while True:
   
    ret, img =cam.read()
    img = cv2.flip(img, 1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        
        #Updating database in real time
        id_list = []
        name_list = []
        id_number_list = []
        conn = sqlite3.connect('Banco_de_dados.db')

        cursor = conn.execute("SELECT ID, NAME, ID_NUMBER from REGISTER")
        for row in cursor:
            id_list.append(int(row[0]))
            name_list.append(row[1])
            id_number_list.append(int(row[2]))

        conn.close()

        #Init rectangle aroud faces
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < confidence_in): #Up to 68% of confidence
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            
            #real time converting values from list
            name = name_list[id]
            id = id_number_list[id]
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id = str(name)
            confidence = "  {0}%".format(round(100 - confidence))

        #Under 68% showing Unknown in video
        elif (confidence < confidence_out):
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
            id = 'Unknown'
            confidence = "  {0}%".format(round(100 - confidence))

        
        #Error condition = frame increment reset
        else:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
            id = 'Error'
            confidence = "  {0}%".format(round(100 - confidence))
            Value_Increment1 = 0
            Value_Increment2 = 0
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Limpar as telas quando sair

cam.release()
cv2.destroyAllWindows()

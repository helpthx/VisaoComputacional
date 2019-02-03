''''
Capture multiple Faces from multiple users to be stored on a DataBase (dataset directory)
    ==> Faces will be stored on a directory: dataset/ (if does not exist, pls create one)
    ==> Each face will have a unique numeric integer ID linked with a SQLite3 database call Banco_de_dados.db
    ==> Each ID has a name, matricula, amount of credit in RU and acessos.


Based on original code by Anirban Kar: https://github.com/thecodacus/Face-Recognition    

Developed by João Vitor Rodrigues Baptista. 

'''

import cv2
import os
import sqlite3

'''
==> Path to convert the database in lists, cos we need a list's ID to link the database and the dataset.

'''

id_list = []
name_list = []
id_number_list = []
money_list = []
acess_list = []
conn = sqlite3.connect('Banco_de_dados.db')
print ('\nDatabase open successfully...')

cursor = conn.execute("SELECT ID, NAME, ID_NUMBER, MONEY, ACCESS from REGISTER")
for row in cursor:
    id_list.append(int(row[0]))
    name_list.append(row[1])
    id_number_list.append(int(row[2]))
    money_list.append(float(row[3]))
    acess_list.append(int(row[4]))


print("Changed successfully...")
conn.close()


cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
#face_id = input('\n Entre com o id do aluno ==>  ')

face_id = id_list[-1]

print("\n[INFO]Beguining the shots. Look to camera and wait...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    img = cv2.flip(img, 1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n[INFO]Done")
cam.release()
cv2.destroyAllWindows()



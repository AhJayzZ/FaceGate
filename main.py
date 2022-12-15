import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from dotenv import load_dotenv
import requests
import pickle
load_dotenv()

# from PIL import ImageGrab

# path = os.getenv("path")
path = "data"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)

# def markAttendance(name):
#     with open('Attendance.csv', 'r+') as f:
#         myDataList = f.readlines()
#         nameList = []
#         for line in myDataList:
#             entry = line.split(',')
#             nameList.append(entry[0])
#         if name not in nameList:
#             now = datetime.now()
#             dtString = now.strftime('%Y %m %d %H:%M:%S')
#             f.writelines(f'\n{name},{dtString}')
    
#   reload pickled data from file
with open('piclist.pkl', 'rb') as f:
    encodeListKnown = pickle.load(f)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
n = 7
while True:
    success, img = cap.read()
# img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] and faceDis[matchIndex]<0.4:
            name = classNames[matchIndex].upper()
            # print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            # markAttendance(name)
            url = os.getenv("url")
            now = datetime.now()
            dtString = now.strftime('%Y/%m/%d %H:%M:%S')
            # print(n)
            if n >= 7:
                try:
                    print(len(requests.get(url+'/api/item/read/'+name).json()))
                    n = 0
                    if len(requests.get(url+'/api/item/read/'+name).json()) == 0:
                        print("post")
                        requests.post(url+'/api/item/create',json={"name":name,"state":"in","in_time":dtString,"out_time":""})
                    else:
                        print("put")
                        requests.put(url+'/api/item/update/'+name,json={"state":"out","out_time":dtString})
                except Exception as e:
                    print(e)
            else:
                n += 1
    cv2.imshow('Webcam', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

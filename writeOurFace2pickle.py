import cv2
import numpy as np
import face_recognition
import os
from dotenv import load_dotenv
import requests
import pickle
import sys
load_dotenv()

# from PIL import ImageGrab

path = os.environ("path")
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
#   write pickled data to file
with open('piclist.pkl', 'wb') as f:
    pickle.dump(encodeListKnown, f)

print('Encoding Complete')



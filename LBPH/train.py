{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "23a4b6c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "training...\n",
      "ok!\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # 載入人臉追蹤模型\n",
    "recog = cv2.face.LBPHFaceRecognizer_create()      # 啟用訓練人臉模型方法\n",
    "faces = []   # 儲存人臉位置大小的串列\n",
    "ids = []     # 記錄該人臉 id 的串列\n",
    "\n",
    "for i in range(1,15):\n",
    "    jpg=\"./face_mama/\"+str(i)+\".jpg\"\n",
    "    img = cv2.imread(jpg)           # 依序開啟每一張的照片\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白\n",
    "    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列\n",
    "    face = detector.detectMultiScale(gray)        # 擷取人臉區域\n",
    "    for(x,y,w,h) in face:\n",
    "        faces.append(img_np[y:y+h,x:x+w])         # 記錄人臉的位置和大小內像素的數值\n",
    "        ids.append(1)                             # 記錄人臉對應的 id，只能是整數，都是 1 表示 id 為 1\n",
    "\n",
    "for i in range(1,15):\n",
    "    jpg=\"./face_yyk/\"+str(i)+\".jpg\"\n",
    "    img = cv2.imread(jpg)           # 依序開啟每一張照片\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 色彩轉換成黑白\n",
    "    img_np = np.array(gray,'uint8')               # 轉換成指定編碼的 numpy 陣列\n",
    "    face = detector.detectMultiScale(gray)        # 擷取人臉區域\n",
    "    for(x,y,w,h) in face:\n",
    "        faces.append(img_np[y:y+h,x:x+w])         # 記錄人臉的位置和大小內像素的數值\n",
    "        ids.append(2)                             # 記錄人臉對應的 id，只能是整數，都是 2 表示的 id 為 2\n",
    "\n",
    "print('training...')                              # 提示開始訓練\n",
    "recog.train(faces,np.array(ids))                  # 開始訓練\n",
    "recog.save('face.yml')                            # 訓練完成儲存為 face.yml\n",
    "print('ok!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f62970f5",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import cv2\n",
    "\n",
    "img = cv2.imread('test.png')           # 依序開啟每一張照片\n",
    "cv2.imshow('test',img) \n",
    "cv2.waitKey(0) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6fb417c2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "626cada5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

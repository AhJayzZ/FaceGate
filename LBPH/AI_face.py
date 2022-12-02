{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8986e8b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "recognizer = cv2.face.LBPHFaceRecognizer_create()         # 啟用訓練人臉模型方法\n",
    "recognizer.read('face.yml')                               # 讀取人臉模型檔\n",
    "cascade_path = \"haarcascade_frontalface_default.xml\"  # 載入人臉追蹤模型\n",
    "face_cascade = cv2.CascadeClassifier(cascade_path)        # 啟用人臉追蹤\n",
    "\n",
    "cap = cv2.VideoCapture(0)                                 # 開啟攝影機\n",
    "if not cap.isOpened():\n",
    "    print(\"Cannot open camera\")\n",
    "    exit()\n",
    "while True:\n",
    "    ret, img = cap.read()\n",
    "    if not ret:\n",
    "        print(\"Cannot receive frame\")\n",
    "        break\n",
    "    img = cv2.resize(img,(540,300))              # 縮小尺寸，加快辨識效率\n",
    "    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # 轉換成黑白\n",
    "    faces = face_cascade.detectMultiScale(gray)  # 追蹤人臉 ( 目的在於標記出外框 )\n",
    "\n",
    "    # 建立姓名和 id 的對照表\n",
    "    name = {\n",
    "        '1':'SBF',\n",
    "        '2':'YYK',\n",
    "    }\n",
    "\n",
    "    # 依序判斷每張臉屬於哪個 id\n",
    "    for(x,y,w,h) in faces:\n",
    "        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)            # 標記人臉外框\n",
    "        idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])  # 取出 id 號碼以及信心指數 confidence\n",
    "        if confidence < 60:\n",
    "            text = name[str(idnum)]                               # 如果信心指數小於 60，取得對應的名字\n",
    "        else:\n",
    "            text = '???'                                          # 不然名字就是 ???\n",
    "        # 在人臉外框旁加上名字\n",
    "        cv2.putText(img, text, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)\n",
    "\n",
    "    cv2.imshow('oxxostudio', img)\n",
    "    if cv2.waitKey(5) == ord('q'):\n",
    "        break    # 按下 q 鍵停止\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "65e49c13",
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

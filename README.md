# 基於人臉辨識的門禁打卡系統 (FaceGate)

## 介紹 Introduction
利用人臉識別技術，實現人員進出和打卡的自動化管理。該系統通過攝像頭捕捉人員面部圖像，並透過AI模型對人臉辨識進行身份驗證，確保只有授權人員才能進入特定區域或完成打卡操作。此系統具有高效便捷、高安全性和非接觸操作的優勢，特別適合於辦公室、學校、工廠和社區等場景。

---
## 研究目的 Purpose
- 課程需進行手動簽到很麻煩，透過人臉辨識直接進行簽到，**減少不必要的人流與步驟**。
- 公司進出或是打卡，可以**減少使用或是遺失公司門禁卡的機率**，同時也可以知道人員現在是否在公司內。

---
## 使用流程 Usage
- Step 0. 上傳清晰正臉照，以作為人臉辨識基礎(30張各自資料集)
- Step 1. 辨識人臉紀錄辨識當下時間及姓名
- Step 2. 上傳辨識資料(姓名、狀態(登入、登出)、時間)至資料庫
- Step 3. 網頁讀取資料庫數據並加以呈現

---
## 展示影片 Demo
[![FaceGate Demo Video](http://img.youtube.com/vi/PMHbNJoS0gE/0.jpg)](http://www.youtube.com/watch?v=PMHbNJoS0gE "FaceGate")
---
## 系統設計 System Design
- ### 架構圖 Architeture
    ![image](https://hackmd.io/_uploads/BJgXwthmC.png)
- ### 流程圖 Flow Chart
    ![image](https://hackmd.io/_uploads/H1DjuK3mA.png)

- ### 人臉辨識系統
    - ### Method 1: LBPH（Local Binary Patterns Histogram）- 局部二進制模式直方圖
        LBPH（Local Binary Patterns Histogram）是一種用於圖像處理和電腦視覺領域的特徵提取方法，特別在面部識別中廣泛應用。

        - 概念 Concept
            - Local Binary Patterns (LBP)：LBP是一種用於描述圖像紋理的算子。它將圖像中的每個像素的灰度值與其鄰域內的像素進行比較，生成二進制數字，然後將這些數字轉換為十進制值，形成局部二值模式。
            - Histogram：LBPH在提取LBP特徵後，會對這些特徵進行統計，生成一個直方圖，表示圖像中不同模式出現的頻率。

        - 流程 Flow
            ![image](https://hackmd.io/_uploads/S1saoYhXC.png)


    - ### Method 2: Dlib 神經網路檢測法
        Dlib是一個用於機器學習、計算機視覺和數據分析的現代C++工具庫，也有Python的接口。它在許多領域中廣泛應用，特別是在面部識別、物體檢測和圖像處理等方面。
        - 功能 Feature
            - 機器學習
                - 提供多種機器學習算法，包括支持向量機（SVM）、K-最近鄰（KNN）、決策樹等。
                - 支持深度學習，內置深度神經網絡（DNN）模型和訓練方法。

            - 面部識別
                - 提供面部檢測、面部對齊、面部特徵點提取和面部識別等功能。
                - 使用高效的HOG（Histogram of Oriented Gradients）特徵描述符和深度學習模型進行面部識別。

            - 物體檢測
                - 支持使用滑動窗口技術和卷積神經網絡（CNN）進行物體檢測。
                - 提供預訓練的模型，可以用於各種物體檢測任務。

            - 圖像處理
                - 支持基本的圖像處理操作，如圖像濾波、邊緣檢測、形態學操作等。
                - 可以與OpenCV等其他圖像處理庫結合使用。

            - 數據分析
                - 提供數據集加載、預處理和可視化工具。
                - 支持多種數據分析和可視化技術。

        - 流程 Flow
            ![image](https://hackmd.io/_uploads/S1j5oF27A.png)

    
- ### 後端API系統開發
    - 開發框架: Flask
        - GET  提供前端網頁獲取資料庫的資料
        - POST 提供人臉辨識系統儲存資料至資料庫
        - PUT  提供人臉辨識系統更新資料
    - 反向代理: Ngrok
        - 內外網溝通代理伺服器
    - 容器化技術: Docker
        - 隔離環境與方便部屬

    - 成果
    ![image](https://hackmd.io/_uploads/H1m9FYhmA.png)

- ### 前端使用者UI開發
    - 開發框架: React
    - 成果
    ![image](https://hackmd.io/_uploads/Bkc-qFnQA.png)

---
## 開發環境 Enviroment
- ### 開發環境 Enviroment
    - 開發版: Raspberry Pi 4
    - 開發環境: Linux Ubuntu 20.04
    
- ### 執行環境 Runtime
    - 後端(Backend)
        - 語言: Python 3.8.10
        - 包管理工具: pip 23.3.1
        - 開發框架: Flask 2.1
    - 前端(Frontend)
        - 語言: Node 19.2.0
        - 包管理工具: npm 9.2.0

- ### 資料庫 Database
    - 資料庫: MySQL 5.7.24
    - 資料庫管理: phpmyadmin 5.2
    
- ### 其他 Others
    - 反向代理: Ngork 3.1.0

---
## 開發人員 Developer
- ### 人臉辨識系統
    紹元、昱寬
- ### 前端UI開發&系統整合 
    勁杰
- ### 後端API開發&資料庫 
    振益
    
---
## 未來展望 Future Expectation
- 需辨識人臉總數量增加時先使用算力較高的設備進行人臉資料庫建設。
- 網站更新可以透過Web Socket去進行狀態與資料即時更新，減少不必要的定時網站刷新請求。
- 架構雲端化，部屬到雲端上可以拓展可用與服務性。

---
## 問題與討論 Discussion
- Q1: LBPH 跟 Dlib 的選擇?
    A1: LBPH 需使用較多data作為數據基礎，而 Dlib 由於是有先前的訓練模型，故只需要一張清晰的正臉照就可以有效的進行辨識。

- Q2: 用Ubuntu 18.04 安裝作業環境及函式庫時，遇到有蠻多問題?
    A2: 改用Debian with Raspberry Pi Desktop。

- Q3: CORS跨網域存取問題?
    A3: 透過Ngork並將前、後端系統放在同一個環境上運作。

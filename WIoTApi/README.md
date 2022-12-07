# WIoTApi
## Overview
docker MySQL, phpMyadmin and database Api
### Port
```
MySQL       3306
phpMyadmin  8080
api server  5000

## Step
### Step 1.
```
sudo apt-get update
sudo apt-get install -y docker.io
# 如果使用root install就不需要執行以下兩行
sudo usermod -aG docker username
sudo reboot
```
重新登入後 docker version確認 docker 是否裝好
### Step 2.
 ```
 git clone https://github.com/AhJayzZ/WirelessIoT.git
 cd WioTApi
 ./build_docker.sh
 ```
 執行完後確認MySQL跟phpMyadmin的container是否啟動，到瀏覽器輸入ip登入phpMyadmin，預設帳號密碼為root:root。
 登入後先創建新的database，名稱openapi。
 修改app_config.py跟create.py內MySQL的ip。
 ### Step 3.
 ```
 ./build_apiSvc.sh
 ```
檢查是否啟動
將swagger.yaml用openapi套件開啟即可確認API

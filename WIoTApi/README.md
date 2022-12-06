# WIoTApi
## Overview
docker MySQL, phpMyadmin and database Api
## Step
### Step 1.
```
sudo apt-get update
sudo apt-get install -y docker.io
sudo usermod -aG docker username
sudo reboot
```
重新登入後 docker version確認 docker 是否裝好
### Step 2.
 ```
 git clone https://github.com/tony11105/WIoTApi.git
 cd WioTApi
 cd shell
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
